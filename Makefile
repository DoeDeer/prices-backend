include .env
export

.PHONY: lint
lint:
	flake8 src/

.PHONY: stop
stop:
	docker compose --profile test --profile local down

.PHONY: run-local
run-local: stop
	docker compose --profile local build
	docker compose --profile local up -d db
	sleep 2
	cd src && POSTGRES_HOST=localhost alembic upgrade head && cd ..
	docker compose --profile local up -d

.PHONY: run-local-db
run-local-db: stop
	docker compose --profile local up -d db

.PHONY: run-test
run-test: stop
	docker compose --profile test build --no-cache
	docker compose --profile test up -d test-db
	sleep 2
	cd src && POSTGRES_HOST=localhost POSTGRES_PORT=5433 alembic upgrade head && cd ..
	docker compose --profile test up --exit-code-from test --abort-on-container-exit test
	docker compose --profile test down
