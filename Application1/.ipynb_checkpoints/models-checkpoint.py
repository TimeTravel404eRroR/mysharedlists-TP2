from django.db import models

# Create your models here.


class Item(models.Model):
    item_name = models.CharField(max_length=20)
    store = models.ForeignKey("Store", on_delete=models.CASCADE)

class Store(models.Model):
    store_name = models.CharField(max_length=20)

    def legth_name(self):
        if len(self.store_name) > 10:
            return len(self.store_name)
        else:
            return 0


class ShopList(models.Model):
    shoplist_name = models.CharField(max_length=20)
    items = models.ManyToManyField(Item, through="ItemShopList", through_fields=("shop_list", "item"))

class ItemShopList(models.Model):
    item = models.ForeignKey(Item)
    shop_list = models.ForeignKey(ShopList)
    quantity = models.IntergrityField()
    already_bought = models.BooleanField()


