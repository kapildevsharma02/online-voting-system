from django.urls import path
from home import views

urlpatterns = [
    path('', views.homepage, name = 'home'),
    path('result/', views.result, name = 'result'),
    path('clear', views.clear, name = 'clear'),
]