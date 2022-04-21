from rest_framework import serializers
from .models import *


class DroneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        # fields = [
        #     'id',
        #     'name',
        #     'brand',
        #     'serial_number',
        #     'created_at',
        #     'updated_at',
        #     'supported_cameras'
        # ]

        fields = '__all__'
        depth = 1


class CameraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Camera

        fields = '__all__'
