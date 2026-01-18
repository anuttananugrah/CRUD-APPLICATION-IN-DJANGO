from django.db import models

# Create your models here.

class ProductModel(models.Model):
    CATEGORY_ITEMS=(
    ('tv','Tv'),
    ('laptop','Laptop'),
    ('mobile','Mobile'),
    ('fridge','Fridge'),
    ('tv','Tv'),
    ('washing_machine','Washing machine')
    )

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    price=models.IntegerField()
    image=models.ImageField(upload_to="Report_image")
    category=models.CharField(max_length=100,choices=CATEGORY_ITEMS)
