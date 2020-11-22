from django.forms import ModelForm
from .models import Booking,contact

class ContactForm(ModelForm):
    class Meta:
        model=contact
        fields='__all__'