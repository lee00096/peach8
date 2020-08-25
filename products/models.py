from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    view_count = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)