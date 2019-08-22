from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='list'),
    path('login/', views.test, name='login'),
    path('question/<int:id>/', views.test, name='question'),
    path('ask/', views.test, name='question'),
    path('popular/', views.test, name='popular'),
    path('new/', views.test, name='new'),
]
