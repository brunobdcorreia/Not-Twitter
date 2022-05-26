from django.urls import path
from NotTwitter.views import dashboard, profile_list, profile

app_name = "NotTwitter"

urlpatterns = [
    path("", dashboard, name='dashboard'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile/<int:pk>', profile, name='profile')
]