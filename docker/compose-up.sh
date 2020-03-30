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

echo "AFTERMATH"
    echo; echo "Print stack containers"
    docker ps | grep -E "$IMAGE_NAME|$CONTAINER_NAME|$API_PORT|IMAGE" --color=always

    echo; echo "Print app .env"
    docker exec -it $CONTAINER_NAME bash -c "cat /app/.env | grep -E 'MONGO_DB_[^=]+' --color=always"

    echo; echo "Run unittest @ mongo basic"
    docker exec -it $CONTAINER_NAME  bash -c "pipenv run pytest -s tests/service/test_mongo.py::Test::test" | grep -E '===.+in' --color=none

    db=`docker exec -it ${CONTAINER_NAME} bash -c "cat /app/.env | grep MONGO_DB_NAME " `;
    echo; cat << EOF

view running container log; ctrl-z to quit log
    cd $sh;  docker-compose logs;          cd - 1>/dev/null
    cd $sh;  docker-compose logs web;      cd - 1>/dev/null
    cd $sh;  docker-compose logs mongodb;  cd - 1>/dev/null

fancy mongo commands
    echo; echo "Print mongo db";         docker exec -it ${CONTAINER_NAME}_mongodb bash -c "mongo --quiet     --eval 'db.getMongo().getDBNames();' ";
    echo; echo "Print mongo collection"; docker exec -it ${CONTAINER_NAME}_mongodb bash -c "mongo --quiet $db --eval 'db.getCollectionNames();' ";
EOF
