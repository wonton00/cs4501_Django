from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'experience.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

      url(r'^api/v1/job/all/$', views.getAllJobs, name='getAllJobs'),
      url(r'^api/v1/job/(?P<jobID>\d+)/$', views.getJob, name='getJob'),
      url(r'^api/v1/login/$', views.login, name='login'),
      url(r'^api/v1/logout/$', views.logout, name='logout'),
      url(r'^api/v1/register/$', views.register, name='register'),
	  url(r'^api/v1/job/n/$', views.createJob, name='createJob'),
	  url(r'^api/v1/search/$', views.search, name='search'),

)