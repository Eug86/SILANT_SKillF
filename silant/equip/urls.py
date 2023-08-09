from django.urls import path
from .views import MachineList, UnauthorizedList, MachineDetail


urlpatterns = [
   path('unauthorized', UnauthorizedList.as_view(), name='machines_short'),
   path('', MachineList.as_view(), name='machines'),
   path('<int:pk>', MachineDetail, name='machine_detail'),
]