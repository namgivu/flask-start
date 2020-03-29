#!/usr/bin/env bash
      sh=$(cd `dirname $BASH_SOURCE` && pwd)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616
app_home=`cd $sh/.. && pwd`

source "$sh/.env"
if [[ -z $IMAGE_NAME ]]; then echo 'Param :IMAGE_NAME is required as $1'; exit 1; fi

docker image rm -f $IMAGE_NAME

docker build  -t $IMAGE_NAME  --file="$sh/Dockerfile"  $app_home
#             #image name     #path of Dockerfile      #set host's folder

echo
docker image ls | grep -E "$IMAGE_NAME|REPO" --color=always
