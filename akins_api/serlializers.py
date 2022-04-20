from rest_framework import serializers
from .models import *


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = (
            'id',
            'name',
            'serial_number',
            'brand',
            'cameras',
            'created_at',
            'update_at'
        )
