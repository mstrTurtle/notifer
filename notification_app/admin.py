from django.contrib import admin

# Register your models here.


from .models import Message, Event

admin.site.register(Message)
admin.site.register(Event)
