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

# TODO: assertions (grep) below can be improved

python main.py --seed=42 \
               --dataset=boston \
               > output.log 2>> error.log
grep -q "3.2029" output.log || (echo "Output 1 does not match expected output" \
                                && cat output.log \
                                && exit 1)

python main.py --seed=42 \
               --dataset=wines \
               --preprocessor-type=min-max \
               --estimator-type=decision-tree \
               > output.log 2>> error.log
grep -q "0.5765" output.log || (echo "Output 2 does not match expected output" \
                                && cat output.log \
                                && exit 2)

python main.py --seed=42 \
               --dataset=red-wine \
               --preprocessor-type=polynomial \
               --polynomial-preprocessor-kwargs='degree: 3, include_bias: False' \
               --estimator-type=linear-regression \
               > output.log 2>> error.log
grep -q "0.9155" output.log || (echo "Output 3 does not match expected output" \
                                && cat output.log \
                                && exit 3)

[ ! -s error.log ] || (echo "File 'error.log' is not empty" && exit 4)

rm output.log error.log

echo "e2e tests passed"
