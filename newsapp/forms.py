from django import forms
from .models import Subscribers,MailMessage

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['email',]