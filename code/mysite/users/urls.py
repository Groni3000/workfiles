from django.urls import path
from .views import signup_view, log_in_view, log_out_view, profile_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('log_in/', log_in_view, name='log_in'),
    path('log_out/', log_out_view, name='log_out'),
    path('profile/<str:username>/', profile_view, name='profile'),
]
