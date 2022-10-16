from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('project', views.project, name='project'),
    path('autor', views.autor, name='autor')
]
