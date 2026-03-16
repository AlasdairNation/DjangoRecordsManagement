from django.db import models
from django.contrib.auth.models import User, Group
#from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    group = models.ForeignKey(Group, models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Record(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
    created_date = models.DateField()
    creator = models.ForeignKey(User,  null=True ,on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Records"

    def __str__(self):
        return self.name