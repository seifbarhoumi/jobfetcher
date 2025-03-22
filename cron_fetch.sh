#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh

conda activate jobfetcher_env

cd /jobfetcher

python -m job_cli fetch job --type-contrat CDI --departement 07 --limit 50 --export-csv

conda deactivate
