from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=5)


class Artist(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    gender = models.CharField(max_length=2)
    birthday = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    signup_date = models.DateField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)


class Work(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    price = models.IntegerField()
    size = models.IntegerField()