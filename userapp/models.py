from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=16)
    address = models.TextField(max_length=300 , null=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="user/profile", null=True)
    updated_at = models.DateTimeField(auto_now=True)
    logout = models.DateTimeField(null=True)
    def __str__(self):
        return self.name

''' ->product->name
       ->product->price
       ->product->image
       ->product->description
       ->product->seller_id
       ->product->category
       ->product->discount
       ->product->salescount
       ->product->rating'''
category_list = [
    ('milk', 'milk'),
    ('curd', 'curd'),
    ('ghee', 'ghee'),
    ('paneer', 'paneer'),
    ('other', 'other'),
]
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product/image", null=True)
    description = models.TextField(max_length=300 , null=True)
    seller_id = models.IntegerField(null=True)
    category = models.CharField(max_length=255,choices=category_list)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    salescount = models.IntegerField(null=True)
    rating = models.IntegerField()
    def __str__(self):
        return self.name


"""
 -> orders->name
    -> orders->price
    -> orders->address
    -> orders->status
    -> orders->user_id
    -> orders->seller_id
    -> orders->order_date
    -> orders->deleverd_date
    -> orders->image"""

order_status_list =[
    ('pending', 'pending'),
    ('delivered', 'delivered'),
    ('cancelled', 'cancelled')
]
class Order(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)    
    address = models.TextField()
    status = models.CharField(max_length=255,choices=order_status_list,default="pending")
    user_id = models.IntegerField(null=True)
    seller_id = models.IntegerField(null=True)
    order_date = models.DateField(null=True)
    delivered_date = models.DateField(null=True)
    image = models.ImageField(upload_to="order/image", null=True)

class Cart(models.Model):
    user_id = models.IntegerField(null=True)
    product_id = models.IntegerField(null=True)
    def __str__(self):
        return self.user_id