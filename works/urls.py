from django.conf.urls import include, url

from works import views

urlpatterns = [
url(r'^$', views.work_list, name='work_list'),
url(r'^new$', views.work_create, name='work_new'),
url(r'^edit/(?P<pk>\d+)$', views.work_update, name='work_edit'),
url(r'^delete/(?P<pk>\d+)$', views.work_delete, name='work_delete'),
]