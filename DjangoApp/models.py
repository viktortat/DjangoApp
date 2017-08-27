from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/dev/ref/models/fields/

from user_profile.models import User

#https://djbook.ru/rel1.9/ref/models/fields.html
class Post(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=30,default='Global')
    is_active = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]






'''
# Отношения многие к одному
class School(models.Model):
    pass

class Student(models.Model):
    school = models.ForeignKey(School)

# Отношение один к одному
class Entry(models.Model):
    pass

class EntryDetail(models.Model):
    entry = models.OneToOneField(Entry)
    details = models.TextField()

# Отношения многие ко многим
class Product(models.Model):
    name = models.CharField()

class Category(models.Model):
    name = models.CharField(
    product =models.ManyToManyField('Product',blank=True,null=True)
    )
'''

