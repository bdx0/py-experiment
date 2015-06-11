#!/bin/bash -

SCRIPT_PATH=$(dirname $(readlink -f $BASH_SOURCE))

export PYTHONPATH=$SCRIPT_PATH/src:$PYTHONPATH
# Defer control.
python -m org.dbd.scilearn $*
read -p "something here ..."
