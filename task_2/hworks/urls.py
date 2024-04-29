from django.urls import path

from . import views

app_name = 'hworks'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('hwork/my_hworks/',  views.my_hworks, name='my_hworks'),
    path('hwork/<str:username>/list/', views.hworks_list, name='hwork_list'),
    path(
        'hwork/create/',
        views.HworkCreate.as_view(),
        name='hwork_create'
    ),
    path(
        'hwork/update/<int:pk>/',
        views.HworkUpdate.as_view(),
        name='hwork_update'
    )
]
