from pyexpat import model
from webbrowser import get
from django.contrib.auth.models import User
from django.db import models
from akins_api.functions import get_modelfieldlist


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
    megapíxeles = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    ordering = ['brand']

    # def __str__(self):
    #     # return 'id:%d: model:%s: brand:%s weight:%d' % (self.id, self.model, self.brand, self.weight)
    #     # get_modelfieldlist is better due to return a list with all fields defined into the model
    #     return get_modelfieldlist(self)

    def __str__(self):
        return self.model


class Drone(models.Model):
    name = models.CharField(max_length=20, blank=False)
    brand = models.CharField(max_length=20, blank=False)
    serial_number = models.CharField(unique=True,  max_length=20, blank=False)
    supported_cameras = models.ManyToManyField(Camera)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}|Serial{self.serial_number}"
