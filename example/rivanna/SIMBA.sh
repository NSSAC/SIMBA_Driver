#!/usr/bin/env bash

set -o xtrace

export SIMBA_PATH=$(realpath $(dirname $(dirname $(dirname $0))))
sbatch $(dirname $0)/SIMBA.sbatch