#!/bin/bash
scripts/shutdown.sh
docker-compose build --no-cache
docker system prune -f