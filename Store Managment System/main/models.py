from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator



class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        MAIN = "MAIN", 'Main'
        SHOP = "SHOP", 'Shop'
    
    base_role = Role.ADMIN
    
    role = models.CharField(max_length=50, choices=Role.choices)
    
    def save(self,*args, **kwargs):
        if not self.pk: 
            self.role = self.base_role
            return super().save(*args, **kwargs)

class MainManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.MAIN)

class Main(User):
    base_role = User.Role.MAIN
    
    main = MainManager()
    
    class Meta:
        proxy = True
        
    def welcome(self):
        return"Only for main"

@receiver(post_save, sender=Main)
def _post_save_receiver(sender,instance,created, **kwargs):
    if created and instance.role == "MAIN":
        MainProfile.objects.create(user=instance)

class MainProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)

class ShopManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.SHOP)

class Shop(User):
    base_role = User.Role.SHOP
    
    shop = ShopManager()
    
    class Meta:
        proxy = True
        
    def welcome(self):
        return"Only for shop"
    
    
    
    

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    code = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    factory_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    receive_main_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    first_add_main_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    main_remain_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    shop_send_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    shop_receive_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    shop_remain_quantity = models.IntegerField(default=0, validators=[MinValueValidator(0)], blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    STATUS_CHOICES = (
        ('ready', 'Ready to Sell'),
        ('pending', 'Pending'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    recorded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name




class ShopProduct(models.Model):
    recorded_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)