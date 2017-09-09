# __author__ = 'chintanpanchamia'
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),

    url('/submit$', views.image_submission, name='image_submission'),
]