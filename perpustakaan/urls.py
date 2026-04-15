from django.urls import path
from . import views

app_name = 'perpustakaan'

urlpatterns = [
    path('', views.perpustakaan_list_public, name='list'),
    path('user/', views.perpustakaan_list, name='user_detail'),
    path('<int:pk>/', views.perpustakaan_public_detail, name='public_detail'),
    path('edit/', views.edit_perpustakaan, name='edit'),
]
