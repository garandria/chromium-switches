#!/bin/bash

src=${1}

echo "| switch | variable |preproc | location |" > README.md
echo "| -------| -------- |------- | -------- |" >> README.md
find ${src} -type f -name "*switch*.cc" -exec python3 main.py "{}" \; \
    | sort  | sed -e 's/^/|/' | sed -e 's/$/|/' | tr ',' '|' >> README.md
