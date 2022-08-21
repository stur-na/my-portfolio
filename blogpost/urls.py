from django.urls import path
from. import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_home, name= 'blog-home'),
    path('details/<id>/<title>/', views.blog_details, name= 'blog-details')
]