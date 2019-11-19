#!/usr/bin/env bash
sh=$(dirname `readlink -f $0`)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616
app_home=`readlink -f $sh/..`

source "$sh/config.sh"
i=$DOCKER_IMAGE_NAME  # i aka image

docker image rm -f $i

docker build  -t $i        $app_home
#             #image name  #path of Dockerfile

docker image ls | grep $i
