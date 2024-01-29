from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20,default='Home@1234', blank=True, null=True)
    phonenumber = models.CharField(max_length=10,default='', blank=True, null=True)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname + " - " + self.email;


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, max_length=255,default=0.00)
    description = models.TextField()
    category = models.CharField(max_length=255)
    image = models.URLField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class CartItem(models.Model):
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField(default=0)
    product_id = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}'s Cart Item - {self.product_id}"    

