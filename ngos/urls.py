from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.index, name='all_schools'),
    path('<int:pk>', views.schoolDetail, name='single_school'),
    path('create/', views.create, name='create_school'),
]
