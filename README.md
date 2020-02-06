# django-listAPI

[![Build Status](https://travis-ci.org/endormi/django-listAPI.svg?branch=master)](https://travis-ci.org/endormi/django-listAPI)
[![Python Version](https://img.shields.io/badge/python-3.7.4-brightgreen.svg?)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-3.0-brightgreen.svg?)](https://www.djangoproject.com/download/)

> API that interacts with a database and manages serialization and deserialization using django rest framework.

## Running the Project Locally

Clone the repository to your local machine:

```sh
git clone https://github.com/endormi/django-listAPI.git
```

Create the database:

```sh
python manage.py migrate
```

### Install requirements

```sh
pip install -r requirements.txt
```

### Launch the interactive shell

```sh
python manage.py shell
```

#### Import these in the interactive shell

```python
from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
from games.models import Game
from games.serializers import GameSerializer
```

Three instances of the game model:

```python
gamedatetime = timezone.make.aware(datetime.now(), timezone.get_current_timezone())
game1 = Game(name='Example 1', release_date=gamedatetime, game_category='Example category', played=False)
game1.save()
game2 = Game(name='Example 2', release_date=gamedatetime, game_category='Example category', played=False)
game2.save()
game3 = Game(name='Example 3', release_date=gamedatetime, game_category='Example category', played=False)
game3.save()
```

Serialize game instances:

```python
game_serializer = GameSerializer(game1)
print(game_serializer1.data)
game_serializer = GameSerializer(game2)
print(game_serializer2.data)
game_serializer = GameSerializer(game3)
print(game_serializer3.data)
```

##### Rendering the attributes into JSON

```python
renderer = JSONRenderer()
rendered_game1 = renderer.render(game_serializer1.data)
print(rendered_game1)
rendered_game2 = renderer.render(game_serializer2.data)
print(rendered_game2)
rendered_game3 = renderer.render(game_serializer3.data)
print(rendered_game3)
```

#### Deserialization

```python
json_string_for_new_game = '{"name": "for example", "release_date": "000"}'
json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")
stream_for_new_game = BytesIO(json_bytes_for_new_game)
parser = JSONParser()
parsed_new_game = parse.parse(stream_for_new_game)
print(parsed_new_game)
```

### HTTP Requests

Running the development server:

```sh
python manage.py runserver
```

#### Using [Curl](https://curl.haxx.se/download.html)

```sh
curl -X GET http://localhost:8000/games/
```

Example response for the HTTP:

```sh
curl -iX GET http://localhost:8000/games/
```

You should see something like this:

```sh
HTTP/1.0 200 OK
Date: Mon, 25 Feb 2019 ...
Server: WSGIServer/0.2 CPython/3.7.2
Content-Type: application/JSON
etc.
```

> Also you should see details for the game objects

#### Using HTTPIE

```sh
http :8000/games/
```

HTTPIE is included in requirements.txt

> You should see similar http response

```sh
http GET :8000/games/
```

It's the same request as the curl command, but in this case HTTP utility will display a colorized output and uses multiple lines to display the JSON response.

## License

The source code is released under the [MIT License](https://github.com/endormi/django-listAPI/blob/master/LICENSE).
