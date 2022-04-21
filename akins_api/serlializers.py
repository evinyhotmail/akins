from dataclasses import fields
from rest_framework import serializers
from .models import *


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'
