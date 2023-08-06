#!/usr/bin/env bash
set -u
set -o pipefail
set -e
# set -x
# v0.1

# my sql akes for ever..
echo "Press [ENTER] to continue"
read -s < /dev/tty

bash runme_lab_2
bash runme_lab_0
bash runme_lab_1
 