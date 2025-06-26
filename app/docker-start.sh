#!/bin/bash
pip freeze > requirements.txt
docker compose build
docker compose stop && docker compose up -d