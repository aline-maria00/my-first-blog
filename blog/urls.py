from django.urls import path #importando função url
from . import views          #e todas as views do blog

urlpatterns = [
    path('', views.post_list, name='post_list'), #atribuindo view, chamada post_list
]

