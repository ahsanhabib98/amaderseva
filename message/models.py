from django.db import models
from django.contrib.auth.models import User
from service.models import *

# Create your models here.

class Messanger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.user.username


class CommentMobilePhone(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(MobilePhone, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentComputing(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Computing, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentTelevision(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Television, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentOthers(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Others, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentApartment(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentEcommerce(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Ecommerce, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title

class CommentEducation(models.Model):
    rate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    service = models.ForeignKey(Education, on_delete=models.CASCADE)

    def __str__(self):
        return self.service.title
