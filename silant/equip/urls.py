from django.urls import path
from .views import machines, tos, claims, MachineList, TOList, ClaimList, UnauthorizedList, MachineDetail, List, typemachine_detail, CreateTypeMachine, DeleteTypeMachine, typemotor_detail, CreateTypeMotor, DeleteTypeMotor, typetranc_detail, CreateTypeTranc, DeleteTypeTranc, typecmost_detail, CreateTypeCmost, DeleteTypeCmost, typevmost_detail, CreateTypeVmost, DeleteTypeVmost, CreateMachine, DeleteMachine, TODetail, CreateTO, DeleteTO, ClaimDetail, CreateClaim, DeleteClaim



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
   path('machines/create', CreateMachine.as_view(), name='machine_create'),
   path('machines/delete/<int:pk>', DeleteMachine.as_view(), name='machine_delete'),
   path('tos/', TOList.as_view(), name='tos'),
   path('tos/<int:pk>', TODetail, name='to_detail'),
   path('tos/create', CreateTO.as_view(), name='to_create'),
   path('tos/delete/<int:pk>', DeleteTO.as_view(), name='to_delete'),
   path('claims/', ClaimList.as_view(), name='claims'),
   path('claims/<int:pk>', ClaimDetail, name='claim_detail'),
   path('claims/create', CreateClaim.as_view(), name='claim_create'),
   path('claims/delete/<int:pk>', DeleteClaim.as_view(), name='claim_delete'),
   path('api/machines', machines),
   path('api/tos', tos),
   path('api/claims', claims),
]