# feedback/urls.py
from django.urls import path, re_path
from feedback import views

urlpatterns = [
    path('list', views.list, name = 'list'),
    path('create', views.create, name = 'create'),
    re_path(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
]