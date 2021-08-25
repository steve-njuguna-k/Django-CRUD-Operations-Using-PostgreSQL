from django.urls import path
from StudentRegister import views

urlpatterns = [
    path('',views.Add_Info, name='Add_Info'),
]