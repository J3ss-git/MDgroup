from django.urls import path, include
from . import views

# Urls for my webpage called MDgroup Funeral
urlpatterns = [
    path('', views.index),
    path('', views.about_page),
    path('',views.contact_page)
 ]