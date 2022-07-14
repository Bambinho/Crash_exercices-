from django.contrib import admin
from django.urls import path
from . import views 

app_name='pizzas'

urlpatterns=[
    #Home page
    path('',views.index,name='index'),
    #Page showing the list of pizzas 
    path('pizzas/',views.pizzas,name='pizzas'),
    #page for topping list for a given pizzas 
    path('pizzas/<int:top_id>/',views.toppings,name='toppings')
]