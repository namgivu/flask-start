#!/usr/bin/env bash
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
a="$SCRIPT_HOME/../../.."; a=$(cd "$a" && pwd); APP_HOME=$a; ROOT="$APP_HOME/../../.."; ROOT=$(cd "$ROOT" && pwd)

source "$SCRIPT_HOME/config.sh"

docker-compose  -f "$SCRIPT_HOME/docker-compose.yml"  up  -d
#                #custom docker-compose          #run as background
#                #ref. https://stackoverflow.com/a/45158964/248616

echo "
view running container log; ctrl-z to quit log
cd $sh; source ./config.sh; docker-compose up; cd - 1>/dev/null
"
