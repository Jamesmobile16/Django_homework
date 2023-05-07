from django.db import models



class Phone(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=250)
    release_date = models.DateField()
    lte_exists = models.BooleanField()








