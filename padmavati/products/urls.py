from django.urls import path
from . import views
from django.conf.urls import url
# from .views import validate_username

urlpatterns = [
    path('', views.index, name='index'),
    url('validate_username/', views.validate_username),
]