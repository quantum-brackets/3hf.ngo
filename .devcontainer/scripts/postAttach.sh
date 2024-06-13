#!/bin/env bash
set -eux

npm install
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
python -m manage runserver
