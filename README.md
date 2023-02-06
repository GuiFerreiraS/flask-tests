## Installing dependencies

```
pip install -r requirements.txt
```

## Swagger address

`http://localhost:5000/swagger-ui`

## Translating

### Creating .pot file

Command to extract strings in the code:

```
pybabel extract -F babel.cfg -o messages.pot .
```

Example to create .po file for pt:

```
pybabel init -i messages.pot -d translations -l pt
```

The command above will create a messages.po file in translations/pt/LC_MESSAGES, the messages need to be translated then run the command below to compile and create .mo files:

```
pybabel compile -d translations
```

To update, create a new messages.pot:

```
pybabel extract -F babel.cfg -o messages.pot .
```

Then let pybabel merge the changes:

```
pybabel update -i messages.pot -d translations
```

## Running

```
flask run
```

## Building docker image

```
docker build -t rest-apis-flask-python .
```

## Running docker container

### With volume

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" --name rnc-container rest-apis-flask-python
```

### Without volume

```
docker run -dp 5000:5000 --name rnc-container rest-apis-flask-python
```
