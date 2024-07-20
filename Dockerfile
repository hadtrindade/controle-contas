FROM --platform=linux/amd64 python:3.10.14-alpine3.20

COPY . /home/app

WORKDIR /home/app


ENV FLASK_APP=controle_contas/app.py
ENV FLASK_ADMIN_SWATCH=cosmo
ENV ADMIN_NAME="Controle de Contas"
ENV SQLALCHEMY_TRACK_MODIFICATIONS=false
ENV WTF_CSRF_ENABLED=true
ENV JWT_COOKIE_CSRF_PROTECT=true
ENV JWT_COOKIE_SECURE=false

RUN pip install -e .

EXPOSE 8000