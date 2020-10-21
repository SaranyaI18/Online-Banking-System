from django.contrib import admin
from django.urls import path
from .views import homeview, displaycustomers, transferview

urlpatterns = [

	
	path('home/', homeview, name ="homepage"),
	path('customers/', displaycustomers, name ="customerpage"),
	path('transfer/',transferview, name="transferpage"),
	
    
]