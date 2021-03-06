# -*- coding: utf-8 -*-
from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{}'.format(self.name)

    @staticmethod
    def autocomplete_search_fields():
        return ('name__exact', 'name__icontains')


class Game(models.Model):
    # Metadata.
    name = models.CharField(max_length=200)
    platform = models.ForeignKey(Platform, null=True, related_name='games')

    # Imagery.
    image_art = models.ImageField('art', blank=True, upload_to='games',
        help_text='16:9 art. Used for backgrounds, etc. Minimum size should be 1280x720.')
    image_boxart = models.ImageField('boxart', blank=True, upload_to='games',
        help_text='8:11 art akin to Twitch. Used for supplimentary display, lists, etc.')

    # Statuses.
    is_abandoned = models.BooleanField('is abandoned?', default=False,
        help_text='Has this game been abandoned for good?')
    is_completed = models.BooleanField('is completed?', default=False,
        help_text='Has this game been completed (if applicable).' )

    def __str__(self):
        return '{}'.format(self.name)

    @staticmethod
    def autocomplete_search_fields():
        return ('name__exact', 'name__icontains')
