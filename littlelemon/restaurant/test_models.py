
from django.test import TestCase
from restaurant.models import Menu

class TestMenu(TestCase):

    def test_get_item(self):

        item = Menu.objects.create(title="IceCream",price=80.0,inventory=100)
        self.assertEqual(str(item),"IceCream : 80.0")