from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    Cateogry = models.CharField(max_length=30, default="")
    subcateogry = models.CharField(max_length=30, default='')
    pub_date = models.DateField()
    price = models.IntegerField(default=0)
    image = models.ImageField(default = "")

    def __str__(self):
        return  self.product_name

class Contact(models.Model):
    query_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=3030, default="")
    email =models.CharField(max_length=5030, default="")
    phone = models.CharField(max_length=5030, default="")
    query = models.CharField(max_length=30030, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    json_items = models.CharField(max_length=303, default="")
    name = models.CharField(max_length=303, default="")
    email = models.CharField(max_length=503, default="")
    phone = models.CharField(max_length=503, default="")
    address1 = models.CharField(max_length=300, default="")
    address2 = models.CharField(max_length=300, default="")
    city = models.CharField(max_length=300, default="")
    state = models.CharField(max_length=300, default="")
    zip = models.CharField(max_length=300, default="")


class Updateorder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=503, default="")
    timestamp = models.DateField(auto_now_add=True)
