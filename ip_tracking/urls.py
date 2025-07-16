from django.urls import path
from .views import sensitive_view

urlpatterns = [
    path('secure-endpoint/', sensitive_view, name='sensitive'),
]
