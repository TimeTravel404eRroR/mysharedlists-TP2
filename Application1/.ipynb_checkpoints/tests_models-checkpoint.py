from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Item, Store

# Create your tests here.

class StoreItemTest(TestCase):
    
    def test_create_item(self):
        # Crée un magasin
        store = Store.objects.create(store_name='marche')
        # Associe un item au magasin
        item1 = Item.objects.create(item_name='orange', store=store)
        item1.save()
        # Récupère l'item depuis la base de données
        item_from_db = Item.objects.get(item_name='orange', store=store)
        self.assertIsNotNone(item_from_db)
        self.assertEquals(item_from_db.item_name, 'orange')
    
    def test_create_item_error(self):
        # Tente de créer un item sans magasin pour provoquer une erreur
        with self.assertRaises(IntegrityError):
            Item.objects.create(item_name='orange')  # Pas de store associé

    def test_create_store_too_long_names(self):
        # Tente de créer un store avec un nom trop long pour provoquer une erreur
        with self.assertRaises(IntegrityError):
            Store.objects.create(store_name='a' * 100)  # Dépasse le max_length de 20

    def test_length_name_store(self):
        # Crée un magasin avec un nom de 15 caractères
        store = Store.objects.create(store_name='a' * 15)
        # Vérifie la méthode length_name
        self.assertEquals(store.length_name(), 15)
