"""Define URL patterns for learning_logs"""
from django.urls import path 

from . import views 

app_name='learning_logs'
urlpatterns=[
   #Home page 
   path('',views.index,name='index'),
   #page that shows all topics 
   path('topics/',views.topics,name='topics'),
   #details for a single page
   path('topics/<int:topic_id>/',views.topic,name='topic'),
   #Adding new topic page
   path('new_topic/',views.new_topic,name='new_topic'),
   #Adding a page for new entry for a given topic 
   path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
   #Adding an entry edit page
   path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry')
]