from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)  # Ajout de on_delete

class Store(models.Model):
    store_name = models.CharField(max_length=20)

    def length_name(self):  # Correction d'une faute de frappe dans "legth_name"
        if len(self.store_name) > 10:
            return len(self.store_name)
        else:
            return 0


class ShopList(models.Model):
    shoplist_name = models.CharField(max_length=20)
    items = models.ManyToManyField(Item, through="ItemShopList", through_fields=("shop_list", "item"))

class ItemShopList(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  # Ajout de on_delete
    quantity = models.IntegerField()
    shop_list = models.ForeignKey(ShopList, on_delete=models.CASCADE)  # Ajout de on_delete
    already_bought = models.BooleanField()
