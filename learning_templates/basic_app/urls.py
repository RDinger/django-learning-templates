from django.conf.urls import url
from basic_app import views

# template tagging
app_name = 'basic_app' # always the name of the application, has to match the term in {% %} in the html

urlpatterns=[
	url(r'^relative/$',views.relative, name='relative'),
	url(r'^other/$', views.other, name='other'),
]