from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=20)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)

class Store(models.Model):
    store_name = models.CharField(max_length=20)

    def legth_name(self):
        return len(self.store_name)