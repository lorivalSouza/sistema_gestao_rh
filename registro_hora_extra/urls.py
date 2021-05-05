from django.urls import path
from .views import HoraExtraList
    #,HoraExtraCreate
    #, EmpresaEdit

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    #path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    #path('editar/<int:pk>/',
         #EmpresaEdit.as_view(), name='edit_empresa'),
]
