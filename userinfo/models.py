from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify

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
    profile_name = models.CharField(unique=True, max_length=50)
    slug = models.SlugField(null=True, blank=True)
    title = models.CharField(max_length=20, choices=title_choice)
    gender = models.CharField(max_length=10, choices=gender_choice)
    division = models.CharField(max_length=10)
    district = models.CharField(max_length=10)
    birth_day = models.DateField()
    phone = models.IntegerField()
    qualification = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.profile_name

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.profile_name:
        instance.slug = slugify(instance.profile_name)

pre_save.connect(pre_save_receiver, sender=Profile)


def post_save_receiver(sender, instance, created, *args, **kwargs):
    if created:
        if not instance.slug and instance.profile_name:
            instance.slug = slugify(instance.profile_name)
            instance.save()

post_save.connect(post_save_receiver, sender=Profile)
