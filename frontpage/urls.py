from django.urls import path
from . import views

#urlpatterns
app_name = 'homepage'
urlpatterns = [
    path('', views.homepage, name= 'home',)
]