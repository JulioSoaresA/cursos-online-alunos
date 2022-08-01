from django.urls import path
from . import views

urlpatterns = [
    path('<int:curso_id>/', views.curso, name='curso'),
    path('matricula/<int:curso_id>/', views.matricula, name='matricula'),
    path('enviado/<int:componente_id>/', views.envia_atividade, name='envia_atividade'),
    path('certificado/<int:curso_id>/', views.gera_certificado, name='gera_certificado'),
    path('valida_certificado/', views.valida_certificado, name='valida_certificado')
]
