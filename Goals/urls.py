from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.goal_list, name='goal_list'),
]