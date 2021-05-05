from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from sistema_gestao_rh import settings

urlpatterns = [
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('empresas/', include('empresas.urls')),
    path('documentos/', include('documentos.urls')),
    path('hora_extra/', include('registro_hora_extra.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
