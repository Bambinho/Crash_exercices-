""" Path to the pages of the webapps"""
from django.urls import path 
from . import views

app_name='meal_plans'
urlpatterns=[
    #Home page 
    path('',views.index,name='index'),
    #Days of the week page 
    path('day/',views.day,name='day'),
    #Page about details of a given meal 
    path('day/<int:day_id>',views.meals,name='meals')

]