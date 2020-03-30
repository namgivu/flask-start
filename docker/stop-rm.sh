#!/usr/bin/env bash
sh=$(cd `dirname $BASH_SOURCE` && pwd)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/.env"
if [[ -z $CONTAINER_NAME ]]; then echo 'Param :CONTAINER_NAME is required as $1'; exit 1; fi

c=${CONTAINER_NAME};       docker stop $c; docker rm $c
c=${CONTAINER_NAME}_mongo; docker stop $c; docker rm $c

yes | docker container prune
