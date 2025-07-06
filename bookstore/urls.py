from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('secular-eclectic-academic-homeschoolers/',views.about,name='about'),
    path('contact-us/',views.contacts,name='contacts'),
    path('ask-blair/',views.ask_blair,name='ask_blair'),
    path('homeschooling-101/',views.homeschooling,name='homeschooling'),
    path('privacy-policy/',views.privacy_policy,name='privacy_policy'),

    
]

