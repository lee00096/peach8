from django.db import models

class Product(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField
    content = models.TextField()
    stock = models.IntegerField
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)