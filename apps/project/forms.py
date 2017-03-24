from django import forms
from .models import Quote
from django.utils.timezone import now


class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = ['quote', 'quoted_by']
        

   