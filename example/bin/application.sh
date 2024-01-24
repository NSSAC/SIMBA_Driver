#!/usr/bin/env bash

STATUS=$(jq '.statusFile' $1 | tr -d '"')

OUT=$(dirname $1)/$(basename $1 .json).out

echo 'hostname:   ' $(hostname) > ${OUT}

echo 'mode:       ' $(jq '.mode' $1) >> ${OUT}
echo 'currentTick: ' $(jq '.currentTick' $1) >> ${OUT}
echo 'currentTime: ' $(jq '.currentTime' $1) >> ${OUT}

echo '{"status": "success"}' > ${STATUS}