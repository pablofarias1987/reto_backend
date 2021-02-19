from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^credito$', views.CreditoList.as_view()),
    url(r'^credito/(?P<pk>[0-9]+)$', views.CreditoDetail.as_view()),

]