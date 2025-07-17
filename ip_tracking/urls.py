from django.urls import path
from .views import home, sensitive_view

urlpatterns = [
    path('', home, name='home'),  # Root URL to home view
    path('secure-endpoint/', sensitive_view, name='sensitive'),
]

