#!/usr/bin/env bash
sh=$(cd `dirname $BASH_SOURCE` && pwd)  # sh aka script_home_folder ref. https://stackoverflow.com/a/337006/248616

source "$sh/.env"
if [[ -z $IMAGE_NAME ]];     then echo 'Param :IMAGE_NAME is required as $1'; exit 1; fi
if [[ -z $CONTAINER_NAME ]]; then echo 'Param :CONTAINER_NAME is required as $1'; exit 1; fi
if [[ -z $API_PORT ]];       then echo 'Param :API_PORT is required as $1'; exit 1; fi

cd $sh
    # prepare network
    echo
    docker network create "${CONTAINER_NAME}_docker_network"

    # run it up
    echo
    docker-compose  -f "$sh/docker-compose.yml"  up  -d
    #                  #custom docker-compose        #run as background
    #                  #ref. https://stackoverflow.com/a/45158964/248616

    echo; echo "WAITING for $CONTAINER_NAME installation ready ..."
        while true; do
            atlas_ready=`docker logs $CONTAINER_NAME 2>&1 | grep -c 'Serving Flask app' `
            if [[ $atlas_ready != 0 ]]; then break; fi
            sleep 1
        done

    # the flask app ready now, printing container log
    echo
    docker-compose logs web

cd - 1>/dev/null

echo
docker ps | grep -E "$IMAGE_NAME|$CONTAINER_NAME|$API_PORT|IMAGE" --color=always

cat << EOF

AFTERMATH
view running container log; ctrl-z to quit log
    cd $sh;  docker-compose logs;          cd - 1>/dev/null
    cd $sh;  docker-compose logs web;      cd - 1>/dev/null
    cd $sh;  docker-compose logs mongodb;  cd - 1>/dev/null

sample mongo call
    docker exec -it ${CONTAINER_NAME}_mongodb bash -c "mongo --eval 'db.getCollectionNames();' "
EOF
