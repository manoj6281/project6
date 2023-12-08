from csk.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('msd/',msd,name='msd'),
    path('jadeja/',jadeja,name='jadeja'),
]