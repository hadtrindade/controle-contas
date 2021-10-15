run:
	FLASK_APP=controle_contas/app.py FLASK_ENV=Development FLASK_DEBUG=True flask run

test: 
	pytest -s -v --cov=controle_contas
	rm controle_contas/controle_contas.db
	FLASK_APP=controle_contas/app.py flask db upgrade
	
black:
	black -l 79 controle_contas
	black -l 79 tests

