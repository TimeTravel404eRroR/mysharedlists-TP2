from django.test import TestCase

class TestIndexViews(TestCase):

    def test_index_view(self):
        client =Client()
        response= client.get(reverse('index_shop'))
        self.assertEquals(response.status_code, 200)

    def test_index_tpl_view(self):
        self.fail('FIXME')