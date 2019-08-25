#################################
#TO DO NEED WRITE CLEAN TEST SUIT
#################################
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Contact
from django.contrib.auth import get_user_model
from django.test import Client



class AnimalTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email='testcase@email.com', password='12345')
        self.name="testlion"
        self.contact=9898989898,
        self.email="roar@email.com"
        c = Client()
        c.login(username='fred', password='secret')
        url = "c_book/add"
        data = {'name':self.name, 'contact':self.contact, 'email': self.email}
        c.post(url, data)

    def test_get_contact(self):
        """test get"""
        get_contact = Contact.objects.filter(email= self.email)
        if get_contact:
            self.assertEqual(get_contact[0].name, 'testlion')
            self.assertEqual(get_contact[0].contact, 9898989898)
        else:
            print ("Failed to add contact")

    def edit_data_setup(self):
        self.contact=9898989800
        self.email= "changed@example.com"
        get_contact = Contact.objects.get(email= self.email)
        get_contact.email = self.email
        get_contact.contact = self.contact

        c = Client()
        url = "edit/"+str(get_contact.id)
        data = {}
        c.post(url, data)

    def test_edit_contact(self):
        """test edit"""
        self.edit_data_setup()
        get_contact = Contact.objects.get(email= self.email)
        self.assertEqual(get_contact.email, 'changed@example.com')
        self.assertEqual(get_contact.contact, 9898989800)

    def delete_data_setup(self):
        self.email= "changed@example.com"
        get_contact = Contact.objects.get(email= self.email)
        c = Client()
        url = "delete/"+str(get_contact.id)
        data = {}
        c.post(url, data)

    def test_edit_contact(self):
        """delete contact"""
        self.delete_data_setup()
        get_contact = Contact.objects.filter(email= self.email)
        self.assertEqual(get_contactl, [])
