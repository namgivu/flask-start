#!/usr/bin/env bash
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
a="$SCRIPT_HOME/.."; a=$(cd "$a" && pwd); APP_HOME=$a; ROOT="$APP_HOME/../../.."; ROOT=$(cd "$ROOT" && pwd)

source "$SCRIPT_HOME/config.sh"
i=$DOCKER_IMAGE_NAME  # i aka image

docker image rm -f $i

docker build  -t $i        $APP_HOME
#             #image name  #path of Dockerfile

docker image ls | grep $i
