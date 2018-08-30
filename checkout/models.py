from django.db import models
from products.models import Product

class Order(models.Model):
    full_name = models.CharField(max_length=50, blank="False")
    phone_number = models.IntegerField(blank="False")
    country = models.CharField(max_length=50, blank="False")
    postcode = models.CharField(max_length=50, blank="False")
    town_or_city = models.CharField(max_length=50, blank="True")
    street_address1 = models.CharField(max_length=50, blank="False")
    street_address2 = models.CharField(max_length=50, blank="True")
    county = models.CharField(max_length=50, blank="True")
    date = models.DateField() 

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=False)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)




