from django.db import models

# Create your models here.

class Division(models.Model):
    division_name = models.CharField(max_length=50)
    def __str__(self):
        return self.division_name

class District(models.Model):
    district_name = models.CharField(max_length=50)
    division = models.ForeignKey(Division,  on_delete=models.CASCADE)
    def __str__(self):
        return self.district_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    category_photo = models.ImageField(upload_to='category_image', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MobilePhone(models.Model):
    condition_choice = (
        ('used','used'),
        ('new','new'),
    )

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    condition = models.CharField(max_length=10, choices=condition_choice)
    brand = models.CharField(max_length=120)
    thtree_g = models.BooleanField(default=False)
    four_g = models.BooleanField(default=False)
    touch_screen = models.BooleanField(default=False)
    description = models.TextField()
    model = models.CharField(max_length=100)
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Computing(models.Model):
    condition_choice = (
        ('used','used'),
        ('new','new'),
    )
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    condition = models.CharField(max_length=10, choices=condition_choice)
    brand = models.CharField(max_length=120)
    desktop = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)
    tablet = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    model = models.CharField(max_length=100)
    configuration = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Television(models.Model):
    condition_choice = (
        ('used','used'),
        ('new','new'),
    )
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    condition = models.CharField(max_length=10, choices=condition_choice)
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Others(models.Model):
    condition_choice = (
        ('used','used'),
        ('new','new'),
    )
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    condition = models.CharField(max_length=10, choices=condition_choice)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Apartment(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    bed = models.IntegerField()
    bathroom = models.IntegerField()
    flat_area = models.CharField(max_length=100)
    address = models.CharField(max_length=130)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Ecommerce(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    warrenty = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    study_choice = (
        ('bangla','bangla'),
        ('english','english'),
    )
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='service_image', blank=True)
    study_item = models.CharField(max_length=10, choices=study_choice)
    description = models.TextField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    designation = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='team_image', blank=True)

    def __str__(self):
        return self.name
