from django.contrib import admin
from django.urls import path,include
from workflow import views
urlpatterns = [
    path("index", views.index, name='index'),
    path("customers", views.customers, name='customers'),
    path("orders", views.orders, name='orders'),
    path("analytics", views.analytics, name='analytics'),
    path("messages", views.messages, name='messages'),
    path("products", views.products, name='products'),
    path("reports", views.reports, name='reports'),
    path("settings", views.settings, name='settings'),
    path("addproducts", views.addproducts, name='addproducts'),
    path("login", views.login, name='login'),
    
]

