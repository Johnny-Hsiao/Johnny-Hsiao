from django.conf.urls import patterns, url

urlpatterns = patterns('about.views', 
	url(r'^$', 'about', name='about'),
)