#!/bin/bash

#SBATCH --job-name test
#SBATCH --time 1:00
#SBATCH --partition bii
#SBATCH --qos bii-half
#SBATCH --account nssac_covid19
#SBATCH --nodes 2
#SBATCH --tasks-per-node 37

hostname