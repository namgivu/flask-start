#!/usr/bin/env bash
sh=$(dirname `readlink -f $0`)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/config.sh"

docker-compose  -f "$sh/docker-compose.yml"  up  -d
#                #custom docker-compose          #run as background
#                #ref. https://stackoverflow.com/a/45158964/248616

echo "
view running container log; ctrl-z to quit log
cd $sh; source ./config.sh; docker-compose up; cd - 1>/dev/null
"
