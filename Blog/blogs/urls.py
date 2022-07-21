from django.urls import path 
from . import views 


app_name='blogs'

urlpatterns=[
    #index page 
    path('',views.index,name='index'),
    #New post page
    path('new_post/',views.new_post,name='new_post'),
    #Page for editing 
    path('edit_post/<int:post_id>/',views.edit_post,name='edit_post')
]