from django.urls import path
from . import views

urlpatterns = [
    path('<int:curso_id>', views.curso, name='curso'),
    path('<int:curso_id>', views.matricula, name='matricula')
]