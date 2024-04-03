from django.urls import path
from .views import *

urlpatterns = [
    path('health_check/', health_check, name='health_check'),
    path('fetch_fact/', fetch_fact, name='fetch_fact'),
    path('get_fact/',get_fact, name='get_fact'),
    path('check/',test_celery_view, name='test_celery_view'),
]
