import pytz
from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Customer(AbstractUser):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=90)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'custom_user'


class Task(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    important = "Important"
    normal = "Normal"
    ty = (
        (important, "Important"),
        (normal, "Normal"),
    )
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    title = models.CharField(max_length=190, null=False, blank=False)
    discription = models.TextField()
    type = models.CharField(max_length=10, choices=ty)
    time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.title
