#!/usr/bin/env bash
sh=$(cd `dirname $BASH_SOURCE` && pwd)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/.env"
if [[ -z $IMAGE_NAME ]];     then echo 'Param :IMAGE_NAME is required as $1'; exit 1; fi
if [[ -z $CONTAINER_NAME ]]; then echo 'Param :CONTAINER_NAME is required as $1'; exit 1; fi
if [[ -z $API_PORT ]];       then echo 'Param :API_PORT is required as $1'; exit 1; fi

cd $sh
    docker-compose  -f "$sh/docker-compose.yml"  up  -d
    #                  #custom docker-compose        #run as background
    #                  #ref. https://stackoverflow.com/a/45158964/248616
cd - 1>/dev/null

docker ps | grep -E "$IMAGE_NAME|$CONTAINER_NAME|$API_PORT|IMAGE" --color=always

echo "
view running container log; ctrl-z to quit log
cd $sh;  docker-compose logs;  cd - 1>/dev/null
"
