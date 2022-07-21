""" Path to the pages of the webapps"""
from django.urls import path 
from . import views

app_name='meal_plans'
urlpatterns=[
    #Home page 
    path('',views.index,name='index'),
    #Days of the week page 
    path('day/',views.day,name='day'),
    #Add new day that will have memues 
    path('new_day/',views.new_day,name='new_day'),
    #Page about details of a given meal 
    path('day/<int:day_id>',views.meals,name='meals'),
    path('day/<int:day_id>/new_meal',views.new_meal,name='new_meal'),
    path('edit_meal/<int:meal_id>',views.edit_meal,name='edit_meal')

]