from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'process-money', views.process_money),
    url(r'^reset$', views.reset),
]