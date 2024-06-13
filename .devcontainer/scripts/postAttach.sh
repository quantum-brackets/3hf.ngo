#!/bin/env bash
set -eux

npm install
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m manage migrate
gh codespace ports visibility 8000:public -c $CODESPACE_NAME
python -m manage runserver
