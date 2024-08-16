from django.urls import path
from .views import registrouser

urlpatterns = [
    path('registrar',registrouser, name='registrouser'),
]
