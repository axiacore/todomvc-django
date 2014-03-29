from django.conf.urls import patterns, include, url

# Function based API views
# from api.views import task_list, task_detail

# Class based API views
from api.views import TaskList, TaskDetail

urlpatterns = patterns('',

    # Regular URLs
	# url(r'^tasks/$', task_list, name='task_list'),
    # url(r'^tasks/(?P<pk>[0-9]+)$', task_detail, name='task_detail'),

    # Class based URLs,
    url( r'^tasks/$', TaskList.as_view(), name = 'task_list' ),
    url( r'^tasks/(?P<pk>[0-9]+)$', TaskDetail.as_view(), name = 'task_detail' ),
)