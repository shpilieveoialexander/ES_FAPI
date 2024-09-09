#! /usr/bin/env sh

# Run pre-start script
bash /backend/bash_scripts/pre_start.sh

# Run server
python /backend/service/main.py