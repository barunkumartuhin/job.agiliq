from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^register', 'job_application.views.job_register', name='job_register'),
    url(r'', 'job_application.views.authorize', name='authorize'),
)
