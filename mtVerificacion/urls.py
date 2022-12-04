from django.urls import path, re_path
from django.conf.urls import include

from mtVerificacion.views import Calculo

urlpatterns = [
    re_path(r'notacion', Calculo.as_view()),    
]