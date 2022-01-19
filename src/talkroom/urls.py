

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'), # 追記
]
handler500 = views.my_customized_server_error