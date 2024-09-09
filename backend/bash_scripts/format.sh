#!/bin/sh -e
set -x

autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place /backend/ --exclude=__init__.py
black /backend/
isort /backend/

chmod a+w /backend -R
