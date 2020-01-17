from django.db import models


class Users(models.Model):
    objects = models.Manager()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=8)
    email = models.EmailField(max_length=100, default='')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Sessions(models.Model):
    key = models.CharField(max_length=8)
    user = models.ForeignKey(Users, null=True, on_delete=models.SET_NULL)
    expires = models.DateTimeField()

    def __str__(self):
        return self.key


