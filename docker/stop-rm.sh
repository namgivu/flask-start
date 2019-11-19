#!/usr/bin/env bash
sh=$(dirname `readlink -f $0`)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/config.sh"

c=$CONTAINER_NAME
printf "Removing $c... "
docker stop $c 1>/dev/null 2>&1
docker rm   $c 1>/dev/null 2>&1
echo 'Done'
