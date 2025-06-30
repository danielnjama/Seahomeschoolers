from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('secular-eclectic-academic-homeschoolers/',views.about,name='about'),
    path('contact-us/',views.contacts,name='contacts'),
    path('privacy-policy/',views.privacy_policy,name='privacy_policy'),

    
]