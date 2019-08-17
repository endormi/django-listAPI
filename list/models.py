from django.db import models


class Game(models.Model):
	name = models.CharField(max_length=200, blank=True, default='')
	release_date = models.DateTimeField()
	game_category = models.CharField(max_length=200, blank=True, default='')

	class Meta:
		ordering = ('name',)