#!/bin/sh

flask db init
flask db migrate
flask db upgrade

export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=8080