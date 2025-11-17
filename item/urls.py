from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.browse_items, name='browse_items'),
    path('new/', views.new_item, name='new_item'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete_item, name='delete_item'),
    path('<int:pk>/edit/', views.edit_item, name='edit_item'),
]
