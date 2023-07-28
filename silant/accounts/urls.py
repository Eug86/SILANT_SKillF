from django.urls import path
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path(r'logout/', LogoutView.as_view(), name='logout')
]