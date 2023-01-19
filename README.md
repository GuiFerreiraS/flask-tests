## Installing dependencies

`pip install -r requirements.txt`

## Swagger

`http://localhost:5000/swagger-ui`

## Running

`flask run`

## Building docker image

`docker build -t rest-apis-flask-python .`

## Running docker container

### With volume

`docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --name rnc-container rest-apis-flask-python`

### Without volume

`docker run -dp 5000:5000 --name rnc-container rest-apis-flask-python`
