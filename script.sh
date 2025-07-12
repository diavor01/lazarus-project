#!/bin/bash

python3 -m venv venv
source venv/bin/activate

git diff --name-only | python3 workflow.py