# get started
Flask ref. https://www.tutorialspoint.com/flask/flask_quick_guide.htm

## direct run
require python 3.7 via pyenv and pipenv ref. bit.ly/nnpipenv

```bash
: you@localhost:/path/to/git/cloned/
pipenv sync
pipenv run python src/app.py
```

## docker run
```bash
: you@localhost:/path/to/git/cloned/
./docker/build.sh 
./docker/compose-up.sh 

: wait until the web app ready to serve e.g. by docker-compose up

# view web at /
http :19111/hi  # should see Hi there!

# stop it
./docker/stop-rm.sh

```

## run test mongo 
# copy .env.sample to .env

```bash
cp .evn.sample .env 
```

```bash
PYTHONPATH=`pwd` pipenv run pytest -s tests/service/test_mongo.py::Test::test
```
