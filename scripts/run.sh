#!/bin/bash
scripts/shutdown.sh
docker-compose up -d && docker-compose logs -f web huey