# Project commands

# launch
start:
	python3 ./src/main.py

test:
	pytest tests/ -v

# docker commands:
docker_build:
	docker-compose up -d --build

docker_stop:
	docker-compose down