from django import forms
from django.utils import timezone
from .models import Message
from django.contrib.admin.widgets import AdminSplitDateTime

class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['send_time', 'email_title', 'email_content', 'status']
    email_title = forms.CharField()
    send_time = forms.DateTimeField(widget = DateTimePickerInput, initial=timezone.now())
    status =  forms.CharField(widget = forms.HiddenInput(), initial='idle')

