up:
	cd docker && docker compose -f docker-compose-local.yaml up -d

down:
	cd docker && docker-compose -f docker-compose-local.yaml down --volumes && docker network prune --force


