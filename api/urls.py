from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('v1/pages/', views.ListUrlView.as_view(), name='list-url-view'),
]
