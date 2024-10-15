from django.urls import path
from . views import Customer_account, Logout_view
urlpatterns = [
    path('',Customer_account, name='account' ),
    path('logout',Logout_view, name='logout'),
]