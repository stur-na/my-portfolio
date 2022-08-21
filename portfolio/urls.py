from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.portfolio_home, name= 'portfoliohome'),
    path('details/<id>/<title>', views.portfolio_details, name = 'portfoliodetails')
]