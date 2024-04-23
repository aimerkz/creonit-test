#!/bin/bash -x

poetry run python3 manage.py migrate --noinput || exit 1

poetry run python3 manage.py loaddata fixtures/user.json && \
poetry run python3 manage.py loaddata fixtures/tree.json

exec "$@"
