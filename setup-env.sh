#!/bin/sh
mkdir -p $HOME/.pythonvenv
python3 -m venv $HOME/.pythonvenv/deploy
source $HOME/.pythonvenv/deploy/bin/activate
export PATH="$HOME/.pythonvenv/deploy/bin:$PATH"
export PYTHONDONTWRITEBYTECODE=1
