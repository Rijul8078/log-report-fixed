#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py
RESULT=$?

if [ $RESULT -eq 0 ]; then
    echo 1 > /logs/verifier/reward.txt
else
    echo 0 > /logs/verifier/reward.txt
fi

echo '{"results":[]}' > /logs/verifier/ctrf.json

exit 0