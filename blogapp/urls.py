from django.urls import path
from . import views

urlpatterns = [
    path('secular-eclectic-academic-blog/',views.blog,name='blog'),
    path('bloginfo/',views.bloginfo,name='bloginfo'),
    

    
]