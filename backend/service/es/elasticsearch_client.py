import logging

from elasticsearch import Elasticsearch, helpers

from db import models
from db.session import DBSession
from service.core import settings
from service.schemas import v1 as schemas_v1

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize Elasticsearch client
es = Elasticsearch(hosts=[f"{settings.ES_HOST}:{settings.ES_PORT}"])

INDEX_NAME = "items"


def create_index():
    if not es.indices.exists(index=INDEX_NAME):
        try:
            es.indices.create(
                index=INDEX_NAME,
                body={
                    "mappings": {
                        "properties": {
                            "id": {"type": "integer"},
                            "title": {"type": "text"},
                            "description": {"type": "text"},
                        }
                    }
                },
            )
            logger.info(f"Created index '{INDEX_NAME}'")
        except Exception as e:
            logger.error(f"Error creating index '{INDEX_NAME}': {e}")


def create_item(item: schemas_v1.PostResponse):
    try:
        es.index(index=INDEX_NAME, id=item.id, body=item.dict())
        logger.info(f"Indexed item with id {item.id}")
    except Exception as e:
        logger.error(f"Error indexing item with id {item.id}: {e}")


def update_item(item: schemas_v1.PostResponse):
    try:
        update_body = {"doc": item.dict()}
        logger.info(f"Updating item in Elasticsearch with ID {item.id}")
        es.update(index=INDEX_NAME, id=item.id, body=update_body)
        logger.info(f"Updated item with id {item.id} in Elasticsearch")
    except Exception as e:
        logger.error(f"Error updating item with id {item.id}: {e}")


def delete_item_from_index(item_id: int):
    try:
        es.delete(index=INDEX_NAME, id=item_id, ignore=[400, 404])
        logger.info(f"Deleted item with id {item_id} from index")
    except Exception as e:
        logger.error(f"Error deleting item with id {item_id} from index: {e}")


def bulk_index():
    # Use DBSession as a context manager for better session management
    try:
        with DBSession() as db:
            items = db.query(models.Post).all()
            actions = [
                {
                    "_index": INDEX_NAME,
                    "_id": item.id,
                    "_source": {
                        "id": item.id,
                        "title": item.title,
                        "description": item.description,
                    },
                }
                for item in items
            ]
            helpers.bulk(es, actions)
            logger.info("Bulk indexing completed.")
    except Exception as e:
        logger.error(f"Error during bulk indexing: {e}")


def ensure_index_exists():
    if not es.indices.exists(index=INDEX_NAME):
        create_index()
