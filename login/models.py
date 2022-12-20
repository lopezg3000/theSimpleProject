from django.db import models


class User(models.Model):
    username = models.EmailField(max_length=200)
    password = models.CharField(max_length=255, default="test")
    date_created = models.DateTimeField('date created')

    def __str__(self):
        return self.username
