from django.urls import path
from .views import MachineList


urlpatterns = [
   path('', MachineList.as_view(), name='machines'),
]