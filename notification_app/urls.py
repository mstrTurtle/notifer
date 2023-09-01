# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('messages/', views.messages_list, name='messages_list'),
    path('message/', views.message_list, name='message_list'),
    path('events/', views.events_list, name='events_list'),
    path('cancel/', views.cancel_message, name='cancel_message'),
]
