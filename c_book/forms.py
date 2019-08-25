from django import forms
from django.forms import ModelForm
from .models import Contact


# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
#
# def validate_even(value):
#     if len(str(value)) != 10:
#         raise ValidationError(
#             _('%(value)s is not an Ten digit contact'),
#             params={'value': value},
#         )
#
# class AddForm(forms.Form):
#     name = forms.CharField(label='Contact Name', max_length=70)
#     contact_no = forms.IntegerField(label='Contact Number', validators=[validate_even])
#     email = forms.EmailField(label='Contact Email')

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact', 'email']
