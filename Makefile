run:
	FLASK_APP=controle_contas/app.py FLASK_ENV=Development FLASK_DEBUG=True flask run

test: 
	pytest -s -v --cov=controle_contas
	
black:
	black -l 79 controle_contas
	black -l 79 tests

