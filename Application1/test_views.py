from django.test import TestCase, Client
from django.urls import reverse

class TestIndexViews(TestCase):

    def test_index_view(self):
        # Initialisation du client
        client = Client()
        # Appel de la vue via son nom dans les URLs
        response = client.get(reverse('index_shop'))
        # Vérifie que le code de statut est 200 (succès)
        self.assertEquals(response.status_code, 200)

    def test_index_tpl_view(self):
        # Initialisation du client
        client = Client()
        # Appel de la vue via son nom dans les URLs
        response = client.get(reverse('index_shop'))
        # Vérifie que le code de statut est 200 (succès)
        self.assertEquals(response.status_code, 200)
        # Vérifie que le bon template est utilisé
        self.assertTemplateUsed(response, 'index.html')  # Remplacez 'index.html' par le nom réel du template
