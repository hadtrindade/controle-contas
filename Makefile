run:
	FLASK_APP=controle_contas/app.py FLASK_ENV=Development flask run

test: 
	pytest -s -v --cov=controle_contas
	
black:
	black -l 79 controle_contas
	black -l 79 tests

rm-db:
	rm controle_contas/controle_contas.db
	FLASK_APP=controle_contas/app.py flask db upgrade

prod:
	FLASK_APP=controle_contas/app.py FLASK_ENV=production flask run

db-postgres:
	sudo docker run -d \
		--name bd_test \
		-e POSTGRES_PASSWORD=postgres \
    	-e PGDATA=/var/lib/postgresql/data/pgdata \
    	-v $(pwd)/bd_test:/var/lib/postgresql/data \
		-p 5432:5432 \
    	postgres:13.1