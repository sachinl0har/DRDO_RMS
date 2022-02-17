from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.index, name='home'),
    path('rooms/', views.dashboard, name='rooms'),
    path('room/<str:pk>/', views.room, name='room'),
    path('bookings/<str:pk>/', views.bookings, name='bookings'),
    path('profile/', views.userProfile, name="user-profile"),
    path('update-user/', views.updateUser, name="update-user"),
]