from django.urls import path,include
from . import views
from .  import *

urlpatterns = [
    path('',views.index,name='index'),
]