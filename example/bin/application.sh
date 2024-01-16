#!/usr/bin/env bash

OUT=$(dirname $1)/$(basename $1 .json).out

echo 'hostname:   ' $(hostname) > ${OUT}

echo 'mode:       ' $(jq '.mode' $1) >> ${OUT}
echo 'targetTick: ' $(jq '.targetTick' $1) >> ${OUT}
echo 'targetTime: ' $(jq '.targetTime' $1) >> ${OUT}
