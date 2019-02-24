[![django-rest-framework](https://www.django-rest-framework.org/img/logo.png)](https://www.django-rest-framework.org/)

# django-gamesAPI

> API that interacts with a database and manages serialization and deserialization using django rest framework.

## Running the Project Locally

Clone the repository to your local machine

```
git clone https://github.com/endormi/django-gamesAPI.git
```

Create the database

```
python manage.py migrate
```

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
>>> from datetime import datetime

>>> from django.utils import timezone

>>> from django.utils.six import BytesIO

>>> from rest_framework.renderers import JSONRenderer

>>> from rest_framework.parsers import JSONParser 

>>> from games.models import Game

>>> from games.serializers import GameSerializer
```

Two instances of the game model:

```
>>> gamedatetime = timezone.make.aware(datetime.now(), timezone.get_current_timezone())

>>> game1 = Game(name='Smurfs Jungle', release_date=gamedatetime, game_category='2D mobile arcade', played=False)
game1.save()

>>> game2 = Game(name='Angry Birds RPG', release_date=gamedatetime, game_category='3D RPG', played=False)
game2.save()
```

Serialize the first game instance (game1):

```
>>> game_serializer = GameSerializer(game1)

>>> print(game_serializer1.data)
```

**game2** serialization is the same.

##### Rendering the attributes into JSON

```
>>> renderer = JSONRenderer()

>>> rendered_game1 = renderer.render(game_serializer1.data)

>>> print(rendered_game1)
```

#### Deserialization

```
>>> json_string_for_new_game = '{"name": "for example", "release_date": "000"}'

>>> json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")

>>> stream_for_new_game = BytesIO(json_bytes_for_new_game)

>>> parser = JSONParser()

>>> parsed_new_game = parse.parse(stream_for_new_game)

>>> print(parsed_new_game)
```

> Fully populated game instance

```
>>> new_game_serializer = GameSerializer(data=parsed_new_game)

>>> if new_game_serializer.is_valid():new_game = new_game_serializer.save()

>>> print(new_game.game)
```

## License

The source code is released under the [MIT License](https://github.com/endormi/django-gamesAPI/blob/master/LICENSE).