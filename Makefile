test:
	docker-compose -f docker-compose-tests.yaml up -d
	sleep 1
	pytest tests
	docker-compose -f docker-compose-tests.yaml down --volumes && docker network prune --force

up:
	docker-compose -f docker-compose.yaml up -d


down:
	docker-compose -f docker-compose.yaml down --volumes && docker network prune --force
