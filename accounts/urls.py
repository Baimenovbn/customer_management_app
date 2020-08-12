from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('customer/<int:id>/', views.customer, name='customer'),
    path('user/', views.userPage, name='user'),
    path('account', views.accountSettings, name='account'),

    path('create_order/<int:id>/', views.createOrder, name='create_order'),
    path('update_order/<int:id>/', views.updateOrder, name='update_order'),
    path('delete_order/<int:id>/', views.deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]