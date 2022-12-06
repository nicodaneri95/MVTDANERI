from django.urls import path
from .views import *

urlpatterns= [
    path("Familiares/", listar_familia),
    path("", inicio),
    path("addfamiliar/", familiar),

]