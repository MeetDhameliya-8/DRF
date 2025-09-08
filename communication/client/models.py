import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass 



class Product(models.Model):
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    stock = models.PositiveIntegerField(default=0)  
    image = models.ImageField(upload_to='products/', blank=True, null=True)  

    @property  
    def in_stock(self): 
        return self.stock > 0 
    
    def __str__(self): 
        return self.name 





class Order(models.Model):
    class StatusChoices(models.TextChoices):
        CONFIRMED = 'confirmed'
        PENDING = 'pending'
        CANCELLED = 'cancelled'

    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
        )
    
    products = models.ManyToManyField(Product, 
                                      through='OrderItem', 
                                      related_name='orders')

    def __str__(self):
        return f"order {self.order_id} by {self.user.username}"


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveBigIntegerField()

    @property 
    def item_subtotal(self):  
        return self.Product.price * self.quantity  
    
    def __str__(self): 
        return f"{self.quantity} x {self.Product.name} in order {self.order.order_id}"






      
