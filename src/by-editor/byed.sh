#!/bin/bash -

SCRIPT_PATH=$(dirname $(readlink -f $BASH_SOURCE))

export PYTHONPATH=$SCRIPT_PATH/src:$PYTHONPATH
# Defer control.
python $SCRIPT_PATH/src/byed/main.py $*
read -p "something here ..."
