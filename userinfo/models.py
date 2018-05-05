from django.db import models
from django.contrib.auth.models import User
from service.models import Division, District

# Create your models here.

class Profile(models.Model):
    title_choice = (
        ('Mr.','Mr'),
        ('Miss','Miss'),
        ('Ms.','Ms.'),
        ('Mrs.','Mrs'),
        ('Ir.','Ir'),
        ('Dr.','Dr'),
        ('Drs','Drs'),
        ('Professor','Professor'),
    )
    gender_choice = (
        ('Male','Male'),
        ('Female','Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image', blank=True)
    profile_name = models.CharField(max_length=50)
    title = models.CharField(max_length=20, choices=title_choice)
    gender = models.CharField(max_length=10, choices=gender_choice)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    birth_day = models.DateField()
    phone = models.IntegerField()
    qualification = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.profile_name
