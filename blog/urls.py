from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^&', views.post_list, name='post_list'),  ## 2.1 버전에서 바뀌었다. path 또는 re_path
    path('', views.post_list, name='post_list'),

]
