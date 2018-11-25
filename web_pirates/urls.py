from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from pirates.views import ListaTesourosView, SalvarTesouro, RemoverTesouro

urlpatterns = [
    path('', ListaTesourosView.as_view(), name='lista_tesouros'),
    path('new', SalvarTesouro.as_view(), name='salvar_tesouro'),
    path('new/<int:id>', SalvarTesouro.as_view(), name='salvar_tesouro'),
    path('delete/<int:id>/', RemoverTesouro.as_view(), name='remover_tesouro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)