#!/bin/bash

source ../venv/bin/activate

python main.py

netlistsvg logical_block_scheme.svg.json

eog out.svg
