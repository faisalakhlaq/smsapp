from django import forms
from .models import Sms


class SendSmsForm(forms.ModelForm):

    class Meta:
        model = Sms
        fields = ('sender_name','receiver','title','text')
