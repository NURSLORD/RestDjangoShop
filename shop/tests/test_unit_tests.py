import json

from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase

from shop.models import Product, Category, SubCategory


class ProductCreateTest(APITestCase):

    # def test_create_product(self):
    #     self.assertEqual(1, 1)

    def test_get_product(self):
        url = reverse('product_apis')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create_sub(self):
        url = reverse('sub_create')
        data = {
            "title": "Nurs",
            "is_active": True,
            "category": 4
        }
        response = self.client.post(url, data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_get_sub(self):
        SubCategory.objects.create(title='nurs', is_active=True)
        url = reverse('sub_apis')
        response = self.client.get(url)
        print(response.data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
