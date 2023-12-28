from django.urls import path
from .views import fazer_apostas

urlpatterns = [
    path("", fazer_apostas, name="fazer_apostas")
]
