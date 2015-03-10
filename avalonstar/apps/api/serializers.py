# -*- coding: utf-8 -*-
from rest_framework import serializers

from apps.broadcasts.models import Broadcast, Host, Raid, Series
from apps.games.models import Game
from apps.subscribers.models import Ticket


class BroadcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Broadcast


class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host


class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid


class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
