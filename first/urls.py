from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('feed/', views.feed, name='feed'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='detail'),
    path('<int:pk>/edit', views.EditItem.as_view(), name='edit'),
    path('<int:pk>/delete', views.DeleteItem.as_view(), name='delete'),
    path('new/', views.NewItem.as_view(), name='new'),
    ]
