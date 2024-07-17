from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('dashboard', dashboard, name='dashboard'),
    path('logout', logout, name='logout'),
    path('create-record', create_record, name='create-record'),
    path('update-record/<int:pk>', update_record, name='update-record'),
    path('dashboard/record/<int:pk>', singleRecord, name='record'),
    path('delete_user/<int:pk>', delete_user, name='delete_user'),
]
