from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Fruit', 'Fruit'),
    ('Vegetables', 'Vegetables'),
    ('Bakery', 'Bakery'),
    ('Dairy', 'Dairy'),
    ('Snacks', 'Snacks'),
    ('Personal Care', 'Personal Care'),
    ('Household and Cleaning', 'Household and Cleaning'),
    ('Pet Care', 'Pet Care'),
    ('Electronics', 'Electronics'),
    ('Stationary', 'Stationary'),
    ('Miscellaneous', 'Miscellaneous'),
)   


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer}-{self.product}'