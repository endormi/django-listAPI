[![django-rest-framework](https://www.django-rest-framework.org/img/logo.png)](https://www.django-rest-framework.org/)

# django-listAPI

[![Python Version](https://img.shields.io/badge/python-3.7.2-brightgreen.svg?)](https://www.python.org/downloads/)
[![Django Version](https://img.shields.io/badge/django-2.1.7-brightgreen.svg?)](https://www.djangoproject.com/download/)
![PyPI - Status](https://img.shields.io/pypi/status/django.svg)

> API that interacts with a database and manages serialization and deserialization using django rest framework.

## Running the Project Locally

Clone the repository to your local machine

```
git clone https://github.com/endormi/django-listAPI.git
```

Create the database

```
python manage.py migrate
```

Makemigrations

```
python manage.py makemigrations
```

See [0001_initial.py](https://github.com/endormi/django-listAPI/blob/master/games/migrations/0001_initial.py).

### Install requirements

```
pip install -r requirements.txt
```

### Launch the interactive shell

```
python manage.py shell
```

#### Import these in the interactive shell

```
from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
from games.models import Game
from games.serializers import GameSerializer
```

Two instances of the game model:

```
gamedatetime = timezone.make.aware(datetime.now(), timezone.get_current_timezone())
game1 = Game(name='Smurfs Jungle', release_date=gamedatetime, game_category='2D mobile arcade', played=False)
game1.save()
game2 = Game(name='Angry Birds RPG', release_date=gamedatetime, game_category='3D RPG', played=False)
game2.save()
```

Serialize the first game instance (game1):

```
game_serializer = GameSerializer(game1)
print(game_serializer1.data)
```

**game2** serialization is the same.

##### Rendering the attributes into JSON

```
renderer = JSONRenderer()
rendered_game1 = renderer.render(game_serializer1.data)
print(rendered_game1)
```

#### Deserialization

```
json_string_for_new_game = '{"name": "for example", "release_date": "000"}'
json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")
stream_for_new_game = BytesIO(json_bytes_for_new_game)
parser = JSONParser()
parsed_new_game = parse.parse(stream_for_new_game)
print(parsed_new_game)
```

> Fully populated game instance

```
new_game_serializer = GameSerializer(data=parsed_new_game)
if new_game_serializer.is_valid():new_game = new_game_serializer.save()
print(new_game.game)
```

### HTTP Requests

Running the development server

```
python manage.py runserver
```

#### Using [Curl](https://curl.haxx.se/download.html)

```
curl -X GET http://localhost:8000/games/
```

Example response for the HTTP

```
curl -iX GET http://localhost:8000/games/
```

You should see something like this:

```
HTTP/1.0 200 OK
Date: Mon, 25 Feb 2019 ...
Server: WSGIServer/0.2 CPython/3.7.2
Content-Type: application/JSON
etc.
```

> Also you should see details for the game objects

#### Using HTTPIE

HTTPIE is included in requirements.txt

```
http :8000/games/
```

> You should see similar http response

```
http GET :8000/games/
```

It's the same request as the curl command, but in this case HTTP utility will display a colorized output and uses multiple lines to display the JSON response.


## License

The source code is released under the [MIT License](https://github.com/endormi/django-listAPI/blob/master/LICENSE).
