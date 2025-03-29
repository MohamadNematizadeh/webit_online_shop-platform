from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class Customer(AbstractUser):
    phone = models.CharField(max_length=20,blank=True , null=True)
    address = models.TextField(blank=True , null=True)
    
    def __str__(self):
        return self.username
    

class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('Home_Decor','دکوراسیون منزل'),
        ('Jewelry','زیورآلات'),
        ('Gifts','هدیه'),
        ('Other','سایر')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=PRODUCT_CATEGORY, default='loafer')
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class ProdutctImage(models.Model):
    image = models.ImageField(upload_to='products/')
    product = models.ForeignKey(Product,related_name="images",on_delete=models.CASCADE)
    
    def __str__(self): 
        return f"Image for {self.product.name}"

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)