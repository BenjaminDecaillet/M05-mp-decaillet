#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'
# why do I bother with the above ?
# http://redsymbol.net/articles/unofficial-bash-strict-mode/

#====================================================================================
#title           : e2e.sh
#description     : run e2e tests
#date            : 2022/09/15
#usage           : e2e.sh
#notes           :
#====================================================================================

echo "Running e2e tests..."

python main.py > output.log 2> error.log
[ -f output.log ] || (echo "File 'output.log' does not exist" && exit 1)
[ -f error.log ] || (echo "File 'error.log' does not exist" && exit 2)
[ ! -s error.log ] || (echo "File 'error.log' is not empty" && exit 3)

rm output.log error.log

echo "e2e tests passed"
