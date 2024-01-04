from django.urls import path
from .views import InvoiceListCreateView, InvoiceRetrieveUpdateDestroyView, InvoiceDetailRetrieveUpdateDestroyView

urlpatterns = [
    path('invoices/', InvoiceListCreateView.as_view(), name='invoice-list-create'),
    path('invoices/<int:pk>/', InvoiceRetrieveUpdateDestroyView.as_view(), name='invoice-detail'),
    path('invoices/<int:pk>/details/', InvoiceDetailRetrieveUpdateDestroyView.as_view(), name='invoice-detail-retrieve-update-destroy'),
]