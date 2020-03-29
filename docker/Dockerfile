FROM namgivu/ubuntu-pipenv:16.04-3.6

# create THIS_APP folder
WORKDIR /app

# copy pip packages
COPY ./Pipfile      .
COPY ./Pipfile.lock .

# force-rebuild tag - change _x to new value to invalidate .venv/ and force a rerun
RUN echo 191120_x

# bundle app source
COPY . .

# copy .env used for dockerized mode - NOTE this .env is in folder bin/docker/ and to link the api container with the postgres container
#COPY ./docker/.env .

# for documentation on port
EXPOSE 5000

# Default command when running container
# Run the api at 8000
CMD cd /app; \
    pipenv --rm; \
    pipenv sync; \
    pipenv run  python src/app.py
