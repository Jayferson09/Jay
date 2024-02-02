from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name="home"),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('store/', views.store, name="store"),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]