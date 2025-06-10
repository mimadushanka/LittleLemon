from urllib import response
from django.test import TestCase
from restaurant.models import Menu
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from rest_framework import status



class MenuViewTest(TestCase):
    def setup(self):
        item_1=Menu.object.create(
            title='Pizza', price=15.99, inventory=50
        )
        item_2 = Menu.objects.create(
            title='Burger', price=10.50, inventory=75
            )
        item_3=Menu.objects.create(
            title='Pasta', price=12.00, inventory=30
        )
    def test_getall(self):
        response=self.client.get(reverse('menu-list'))
        menus=Menu.objects.all()
        serialized=MenuSerializer(menus,many=True)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,serialized.data)

        