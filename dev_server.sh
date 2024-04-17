#!/bin/bash

pkill -f 'http.server'

set -euxo

source /Users/juliette/src/.venv/bin/activate

python3 -m http.server --directory static &
watchmedo shell-command \
    --patterns="*.html" \
    --recursive \
    --command='python3 compile_templates.py' \
    ./templates