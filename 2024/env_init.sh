#!/bin/bash
pyenv install 3.11.4
pyenv shell 3.11.4
python3 -m venv .ve
source ./.ve/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt