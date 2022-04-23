from rest_framework import serializers
from .models import *


class CameraSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Camera

        fields = '__all__'


class DroneSerializer(serializers.ModelSerializer):

    cameras = CameraSerializer(many=True)

    # method to get or create a camera
    def get_or_create_cameras(self, cameras):
        camera_ids = []
        for camera in cameras:
            camera_instance, created = Camera.objects.get_or_create(
                pk=camera.get('id'), defaults=camera)
            camera_ids.append(camera_instance.pk)
        return camera_ids

    # method to get or create a camera
    def create_or_update_cameras(self, cameras):
        camera_ids = []
        for camera in cameras:
            camera_instance, created = Camera.objects.update_or_create(
                pk=camera.get('id'), defaults=camera)
            camera_ids.append(camera_instance.pk)
        return camera_ids

    # overwriting create method and create a new camera item
    def create(self, validated_data):
        cameras = validated_data.pop('cameras', [])
        drone = Drone.objects.create(**validated_data)
        drone.cameras.set(self.get_or_create_cameras(cameras))
        return drone

    # overwriting create method and create a new camera item
    def update(self, instance, validated_data):
        cameras = validated_data.pop('cameras', [])
        instance.cameras.set(self.create_or_update_cameras(cameras))
        fields = ['name', 'brand', 'serial_number']
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()
        return instance

    class Meta:
        model = Drone
        fields = [
            'id',
            'name',
            'brand',
            'serial_number',
            'created_at',
            'updated_at',
            'cameras'

        ]
        # to show more filed into the m2m relation
        depth = 1
