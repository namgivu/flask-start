#!/usr/bin/env bash
sh=$(cd `dirname $BASH_SOURCE` && pwd)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/.config.sh"
if [[ -z $CONTAINER_NAME ]]; then echo 'Param :CONTAINER_NAME is required as $1'; exit 1; fi

docker stop $CONTAINER_NAME
docker rm   $CONTAINER_NAME

yes | docker container prune
