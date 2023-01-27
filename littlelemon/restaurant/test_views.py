
from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemView
import requests

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="IceCream",price=80.00,inventory=100)
        Menu.objects.create(title="CreamIce",price=100.00,inventory=80)
        return super().setUp()

    def test_getall(self):
        menu =Menu.objects.all()
        for item,true_item in zip(menu,('IceCream : 80.00','CreamIce : 100.00')):
            self.assertEqual(str(item),true_item)