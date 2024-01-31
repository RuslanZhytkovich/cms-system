up:
	cd docker && docker compose -f docker-compose-local.yaml up -d

down:
	cd docker && docker compose -f docker-compose-local.yaml down && docker network prune --force

