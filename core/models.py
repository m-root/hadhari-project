from django.contrib.gis.db import models

from authentication.models import Account
# Create your models here.


class Organisation(models.Model):
    id = models.CharField(max_length=100,unique=True,primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Admin(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Category(models.Model):
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Location(models.Model):
    coordinate = models.PointField(srid=4326)
    accuracy = models.IntegerField(default=0)

    def __str__(self):
        return '{}'.format(self.coordinate)


class Owner(models.Model):
    name = models.CharField(max_length=255)
    literate = models.IntegerField()
    phone_number = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Daycare(models.Model):
    serial_number = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    established_date = models.DateField(blank=True, null=True)
    max_capacity = models.IntegerField(blank=True, null=True)
    avg_children = models.IntegerField(blank=True, null=True)
    helpers = models.IntegerField(blank=True, null=True)
    standards = models.CharField(max_length=5, blank=True, null=True)
    slug = models.CharField(max_length=255)
    status = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    email = models.CharField(max_length=255, blank=True, null=True)
    cell_phone = models.CharField(max_length=15, blank=True, null=True)
    land_line = models.CharField(max_length=15, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,null=True,blank=True)

    location = models.OneToOneField(Location,models.CASCADE)
    services = models.ManyToManyField(Service)
    categories = models.ManyToManyField(Category)

    organisation = models.ForeignKey(Organisation,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=255)

    file = models.ImageField(upload_to='daycares')
    daycare = models.ForeignKey(Daycare, models.CASCADE)
    visible = models.BooleanField(default=True)

    weight = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(Account,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Contact(models.Model):
    daycare = models.ForeignKey(Daycare, models.DO_NOTHING)
    phone = models.CharField(max_length=8,unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.phone