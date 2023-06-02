"""client_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clientadminapp import views

urlpatterns = [
    path('', views.home,name="home"),
    
    path('dashboard', views.HomePage,name="dashboard"),
    path('products', views.ProductPage,name="products"),
    path('portfolio', views.PortfolioPage,name="portfolio"),
    path('members', views.MembersPage,name="members"),
    path('roles', views.RolesPage,name="roles"),
    path('levels', views.LevelsPage,name="levels"),
    path('layers', views.LayersPage,name="layers"),
    path('logout', views.LogoutPage,name="logout"),
]
