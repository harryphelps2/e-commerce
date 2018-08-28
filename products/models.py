from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=234)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='img')
    stock = models.IntegerField()

    def __str__(self):
        return self.name
    