from django.urls import path

from . import views

app_name = 'hworks'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('hwork/my_hworks/',  views.my_hworks, name='my_hworks'),
    path('hwork/list/', views.HworkList.as_view(), name='hwork_ist'),
    path('hwork/<str:username>/list/', views.hworks_user_list, name='hwork_user_list'),
    path(
        'hwork/create/',
        views.HworkCreate.as_view(),
        name='hwork_create'
    ),
    path(
        'hwork/update/<int:pk>/',
        views.HworkUpdate.as_view(),
        name='hwork_update'
    ),
    path('hwork/hwork_archive/<int:pk>/',  views.hwork_archive_view, name='hwork_archive'),
    path('order/list/', views.orders_list_view, name='orders_list'),
    path('order/order_ready/<int:pk>/', views.order_ready_view, name='order_ready'),
    path('order/order_finished/<int:pk>/', views.order_finished_view, name='order_finished'),
    path('order/create_order/<int:pk>/', views.create_order_view, name='create_order'),
]
