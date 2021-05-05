from django.urls import path
from .views import FuncionariosList, FuncionariosEdit, FuncionariosDelete, FuncionarioCreate

urlpatterns = [
    path('novo', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('', FuncionariosList.as_view(), name='list_funcionario'),
    path('editar/<int:pk>/',
         FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/',
         FuncionariosDelete.as_view(), name='delete_funcionario'),
]
