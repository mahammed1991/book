# pages/urls.py
from django.urls import path

from .views import contact_add, get_all_contacts, get_search_contacts, delete_contact, edit_contact

urlpatterns = [
    path('add', contact_add, name='contact_add'),
    path('delete/<int:contact_id>/', delete_contact, name='contact_add'),
    path('edit/<int:contact_id>/', edit_contact, name='edit_contact'),
    path('get_all_contacts', get_all_contacts, name='get_all_contacts'),
    path('search', get_search_contacts, name='get_search_contacts'),
]
