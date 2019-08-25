from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#from users.models import CustomUser
# Create your models here.
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if len(str(value)) != 10:
        raise ValidationError(
            _('%(value)s is not an Ten digit contact'),
            params={'value': value},
        )

class Contact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField( max_length=70)
    contact = models.IntegerField( validators=[validate_even])
    email = models.EmailField(unique=True)

    def __str__(self):
        return 'Contact: ' + self.name
