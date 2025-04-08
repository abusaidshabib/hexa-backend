from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.title


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product")
    thumbnail = models.BooleanField(default=False)

    def __str__(self):
        return self.product.title
