from django.urls import path
from StudentRegister import views

urlpatterns = [
    path('',views.Index, name='Index'),
]