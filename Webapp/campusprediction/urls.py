
from .import views
from django.urls import path

urlpatterns = [
    path('',views.userlogin),
    path('prediction/',views.prediction),
    
]
