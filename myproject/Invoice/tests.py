from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        # Set up test data
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        self.invoice_detail_data = {'invoice': self.invoice.id, 'description': 'Test Description', 'quantity': 2, 'unit_price': 10.0, 'price': 20.0}

    def test_create_invoice(self):
        url = reverse('invoice-list-create')
        data = {'date': '2024-01-01', 'customer_name': 'Test Customer'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add similar test cases for other CRUD operations

class InvoiceDetailAPITestCase(APITestCase):
    def setUp(self):
        # Set up test data
        self.invoice = Invoice.objects.create(date='2024-01-01', customer_name='Test Customer')
        self.invoice_detail = InvoiceDetail.objects.create(invoice=self.invoice, description='Test Description', quantity=2, unit_price=10.0, price=20.0)

    def test_create_invoice_detail(self):
        url = reverse('invoice-detail-list-create')
        response = self.client.post(url, self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Add similar test cases for other CRUD operations
