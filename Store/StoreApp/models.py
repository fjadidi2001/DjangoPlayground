from django.db import models


class StoreModel(models.Model):
    Price = models.FloatField(max_length=50)
    Discount = models.IntegerField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __float__(self):
        return self.Price

