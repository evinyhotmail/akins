from pyexpat import model
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


# fk	field	models.ForeignKey()
# m2m	field	models.ManyToManyField()
# o2o	field	models.OneToOneField()


#  I just extended the Base Django user to add is_user_support field
# in order control if the user is type support or base
# TODO: in the future is better to create a model with type of user or simple use Django standard groups.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_user_support = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Camera(models.Model):
    model = models.CharField(max_length=20, blank=False, default="")
    brand = models.CharField(max_length=20, blank=False, default="")
    weight = models.PositiveIntegerField(blank=False, default=0)
    dimensions_folded = models.CharField(
        max_length=20, blank=False, default="mm")
    dimensions_unfolded = models.CharField(
        max_length=20, blank=False, default="")
    megapíxeles = models.PositiveIntegerField(
        verbose_name="Megapixel", default=0)
    video_resolution = models.CharField(max_length=20, blank=False, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model


class Drone(models.Model):
    name = models.CharField(max_length=20, blank=False)
    serial_number = models.CharField(unique=True,  max_length=20, blank=False)
    #camera = models.ForeignKey(Camera, on_delete=models.SET_NULL, null=True)
    cameras = models.ManyToManyField(Camera)
    brand = models.CharField(max_length=20, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}|Serial{self.serial_number}"
