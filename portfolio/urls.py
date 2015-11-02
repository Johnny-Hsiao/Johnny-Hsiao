from django.conf.urls import patterns, url

urlpatterns = patterns('portfolio.views', 
	url(r'^$', 'portfolio', name='portfolio'),
)