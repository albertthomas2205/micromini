from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)

class ProductUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    product_id = models.IntegerField()

    class Meta:
        unique_together = ('user_id', 'product_id')
