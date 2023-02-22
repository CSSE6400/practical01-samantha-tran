#!/bin/bash
#
# Validate that the repository has the following structure:
# -- README.md
# -- Pipfile
# -- Pipfile.lock
# -- todo
#    | -- __init__.py
#    | -- views
#         | -- routes.py

failed=0
for file in README.md Pipfile Pipfile.lock; do
    if [ ! -f "$file" ]; then
        echo "FAIL: Missing $file"
        failed=1
    fi
done

if [ ! -d todo ]; then
    echo "FAIL: Missing todo directory"
    failed=1
fi

for file in todo/__init__.py todo/views/routes.py; do
    if [ ! -f "$file" ]; then
        echo "FAIL: Missing $file"
        failed=1
    fi
done

if [ $failed -eq 1 ]; then
    echo "Repository structure is not valid. Please fix the errors above."
    exit 1
fi

