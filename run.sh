#!/bin/bash -x
cp env.example .env
docker-compose up -d || exit 1
exec "$@"
