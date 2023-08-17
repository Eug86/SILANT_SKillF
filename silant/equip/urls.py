from django.urls import path
from .views import MachineList, UnauthorizedList, MachineDetail, List, typemachine_detail, CreateTypeMachine, DeleteTypeMachine, typemotor_detail, CreateTypeMotor, DeleteTypeMotor, typetranc_detail, CreateTypeTranc, DeleteTypeTranc, typecmost_detail, CreateTypeCmost, DeleteTypeCmost, typevmost_detail, CreateTypeVmost, DeleteTypeVmost


urlpatterns = [
   path('unauthorized', UnauthorizedList.as_view(), name='machines_short'),
   path('', MachineList.as_view(), name='machines'),
   path('<int:pk>', MachineDetail, name='machine_detail'),
   path('list', List, name='list'),
   path('typemachines/<int:pk>', typemachine_detail, name='typemachine_detail'),
   path('typemachines/create', CreateTypeMachine.as_view(), name='typemachine_create'),
   path('typemachines/delete/<int:pk>', DeleteTypeMachine.as_view(), name='typemachine_delete'),
   path('typemotors/<int:pk>', typemotor_detail, name='typemotor_detail'),
   path('typemotors/create', CreateTypeMotor.as_view(), name='typemotor_create'),
   path('typemotors/delete/<int:pk>', DeleteTypeMotor.as_view(), name='typemotor_delete'),
   path('typetrancs/<int:pk>', typetranc_detail, name='typetranc_detail'),
   path('typetrancs/create', CreateTypeTranc.as_view(), name='typetranc_create'),
   path('typetrancs/delete/<int:pk>', DeleteTypeTranc.as_view(), name='typetranc_delete'),
   path('typecmosts/<int:pk>', typecmost_detail, name='typecmost_detail'),
   path('typecmosts/create', CreateTypeCmost.as_view(), name='typecmost_create'),
   path('typecmosts/delete/<int:pk>', DeleteTypeCmost.as_view(), name='typecmost_delete'),
   path('typevmosts/<int:pk>', typevmost_detail, name='typevmost_detail'),
   path('typevmosts/create', CreateTypeVmost.as_view(), name='typevmost_create'),
   path('typevmosts/delete/<int:pk>', DeleteTypeVmost.as_view(), name='typevmost_delete'),
]