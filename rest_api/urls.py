from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('', home, name="home"),
    path('krosovka-api/', krosovksMakeAPI),
    path('krosovka-api/<int:pk>/', singleAPI)
]
