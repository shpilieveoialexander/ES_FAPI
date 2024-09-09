from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy import delete, select, update

from db import models
from db.session import DBSession, get_session
from service.es.elasticsearch_client import (INDEX_NAME, create_item,
                                             delete_item_from_index, es,
                                             update_item)
from service.schemas import v1 as schemas_v1

router = APIRouter()


# Create a new item
@router.post(
    "/",
    response_model=schemas_v1.PostResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_post(
    input_data: schemas_v1.PostCreate, session: DBSession = Depends(get_session)
):
    post = models.Post(
        title=input_data.title,
        description=input_data.description,
    )
    with session() as db:
        db.add(post)
        db.commit()
        db.refresh(post)

    create_item(schemas_v1.PostResponse.from_orm(post))

    return post


@router.get("/", response_model=Page[schemas_v1.PostResponse])
def get_posts(session: DBSession = Depends(get_session)):
    posts_query = select(models.Post)
    with session() as db:
        return paginate(db, posts_query)


@router.get("/{post_id}", response_model=schemas_v1.PostResponse)
def get_post_by_id(post_id: int, session: DBSession = Depends(get_session)):
    post_query = select(models.Post).where(models.Post.id == post_id)
    with session() as db:
        post = db.scalars(post_query).one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=schemas_v1.PostResponse)
def update_post(
    post_id: int,
    input_data: schemas_v1.PostUpdate,
    session: DBSession = Depends(get_session),
):
    post_query = select(models.Post).where(models.Post.id == post_id)
    with session() as db:
        post = db.scalars(post_query).one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    new_data = input_data.dict(exclude_unset=True)

    update_post_query = (
        update(models.Post).where(models.Post.id == post_id).values(**new_data)
    )

    with session() as db:
        db.execute(update_post_query)
        db.commit()
        updated_post = db.scalars(post_query).one_or_none()
    updated_post_response = schemas_v1.PostResponse.from_orm(updated_post)

    # Update the item in Elasticsearch
    update_item(updated_post_response)

    return updated_post_response


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, session: DBSession = Depends(get_session)):
    post_query = select(models.Post).where(models.Post.id == post_id)
    with session() as db:
        post = db.scalars(post_query).one_or_none()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    delete_query = delete(models.Post).where(models.Post.id == post_id)
    with session() as db:
        db.execute(delete_query)
        db.commit()

    # Remove the item from Elasticsearch
    delete_item_from_index(post_id)

    return


@router.get("/search/", response_model=Page[schemas_v1.PostResponse])
async def search_posts(query: str, session: DBSession = Depends(get_session)):
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["title", "description"],
            }
        }
    }

    response = es.search(index=INDEX_NAME, body=search_body)
    hits = response.get("hits", {}).get("hits", [])
    item_ids = [int(hit["_id"]) for hit in hits]

    if not item_ids:
        posts_query = select(models.Post).where(models.Post.id == -1)
        with session() as db:
            return paginate(db, posts_query)

    posts_query = select(models.Post).where(models.Post.id.in_(item_ids))
    with session() as db:
        return paginate(db, posts_query)
