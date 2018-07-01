from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('podcasts/', views.PodcastList.as_view(), name='podcast_list'),
    path('newpodcast/', views.NewPodcast.as_view(), name='podcast_new'),
    path('podcast/<int:pk>/', views.PodcastItems.as_view(), name='podcast_items'),
    path('feed/', views.feed, name='feed'),
    path('<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('<int:pk>/edit', views.EditItem.as_view(), name='item_edit'),
    path('<int:pk>/delete', views.DeleteItem.as_view(), name='item_delete'),
    path('newitem/', views.NewItem.as_view(), name='item_new'),
    ]
