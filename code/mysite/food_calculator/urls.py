from django.urls import path
from .views import evaluate


urlpatterns = [
    path('', evaluate, name='eval'),
]