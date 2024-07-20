.PHONY: run test docker-build db migrate clean fmt lint

include ./contrib/.env-sample

run:
	FLASK_DEBUG=true flask run --debug

test: 
	FLASK_DEBUG=true flask drop-db
	pytest -s -v --cov=controle_contas --cov-report=html

docker-build:
	 docker build --pull --rm  -t cc:latest .

compose:
	docker compose up -d

db:
	docker run --rm -d \
		--name db-dev \
		-e POSTGRES_PASSWORD=postgres \
    	-e PGDATA=/var/lib/postgresql/data/pgdata \
		-p 5432:5432 \
    	postgres

migrate:
	flask db upgrade
	flask create-admin-user

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf tests/.pytest_cache

fmt:
	@isort --profile=black -m 3 controle_contas tests --line-length=79
	@black -l 79 controle_contas tests setup.py

lint: fmt
	@isort --profile=black -m 3 --check --diff --line-length=79 controle_contas tests
	@black --check --diff --line-length=79 controle_contas tests
	@flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	@flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics