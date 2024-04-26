from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.index, name="about"),
    path('faq', views.index, name="faq"),
    path('home', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('listing', views.listing, name="listings"),
    path('login', views.login, name="login"),
    path('register', views.registerP, name="register"),
    path('search', views.search, name="search"),
    path('view_property', views.view_property, name=f"view_property"),
    path('aftersignup', views.register, name="aftersignup"),
    path('afterlogin', views.validateUser, name="afterlogin")
]
