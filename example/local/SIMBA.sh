#!/usr/bin/env bash
# set -o xtrace

SIMBA_PATH=$(realpath $(dirname $(dirname $(dirname $0))))

export PYTHONPATH=${SIMBA_PATH}:${PYTHONPATH}
${SIMBA_PATH}/SIMBA.py ${SIMBA_PATH}/example/local