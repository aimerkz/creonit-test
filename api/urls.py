from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('v1/test/', views.test, name='test'),
]
