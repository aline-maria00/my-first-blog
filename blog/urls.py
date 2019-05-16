from django.urls import path #importando função url
from . import views          #e todas as views do blog

urlpatterns = [
    path('', views.post_list, name='post_list'), #atribuindo view, chamada post_list
    path('post/<int:pk>/', views.post_detail, name='post_detail'), #criar uma nova url que aponta para post_detail
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]