run:
	FLASK_APP=controle_contas/app.py FLASK_ENV=development flask run

test: 
	FLASK_APP=controle_contas/app.py FLASK_ENV=development flask drop-db
	pytest -s -v --cov=controle_contas
	
test-cov-report:
	FLASK_APP=controle_contas/app.py FLASK_ENV=development flask drop-db
	pytest -s -v --cov=controle_contas --cov-report=html

black:
	black -l 79 controle_contas
	black -l 79 tests

prod:
	gunicorn "controle_contas.app:create_app()" --log-file -

db:
	sudo docker run -d \
		--name bd_test \
		-e POSTGRES_PASSWORD=postgres \
    	-e PGDATA=/var/lib/postgresql/data/pgdata \
    	-v /tmp:/var/lib/postgresql/data \
		-p 5432:5432 \
    	postgres:13.1

migrate:
	flask db migrate
	flask db upgrade

clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf .pytest_cache
	rm -rf build
	rm -rf dist
	rm -rf *egg-info
	rm -rf *tox/
	rm -rf docs/_build
	rm -rf tests/.pytest_cache
