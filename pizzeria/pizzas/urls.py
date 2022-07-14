from django.urls import path

from . import views

app_name='pizzas'

urlpatterns=[
    #Home page
    path('',views.index,name='index'),
    #Page Showing the name of the availble pizzas 
    path('pizzas/',views.pizzas, name='pizzas'),
    #Page showing the topping for a given pizza 
    path('pizzas/<int:top_id>/',views.topping,name='topping')

]