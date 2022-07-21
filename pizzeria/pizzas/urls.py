from django.urls import path

from . import views

app_name='pizzas'

urlpatterns=[
    #Home page
    path('',views.index,name='index'),
    #Page Showing the name of the availble pizzas 
    path('pizzas/',views.pizzas, name='pizzas'),
    #Page showing the topping for a given pizza 
    path('pizzas/<int:pizza_id>/',views.topping,name='topping'),
    # Adding a new pizza
    path('new_pizza/',views.new_pizza,name='new_pizza'),
    #Adding a topping 
    path('pizzas/<int:pizza_id>/new_top/',views.new_top,name='new_top'),
    #Edit topping 
    path('pizza/<int:top_id>/edit_top/',views.edit_top,name='edit_top')
]