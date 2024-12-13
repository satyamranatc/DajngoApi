from django.urls import path
from .import views

urlpatterns = [
    path('',views.Home),
    path('api/Users',views.Users),
    path('api/Users/<int:id>', views.OneUser),

]
