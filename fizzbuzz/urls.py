from django.conf.urls import url
from fizzbuzz import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^fizzbuzz/GET/$', views.get),
    url(r'fizzbuzz/GET/(?P<pk>[0-9]+)/$', views.getI),	
	url(r'fizzbuzz/POST/(?P<pk>.*)/$', views.post, name='post'),

	url(r'fizzbuzz/SWISS/(?P<pk>.*)/$', views.swiss),
	url(r'fizzbuzz/SWISS/(?P<pk>[ 0-9]+)/$', views.swiss),
	url(r'fizzbuzz/SWISS/$', views.swiss),
	
	url(r'fizzbuzz/demo/(?P<pk>.*)/$', views.demo),

]
urlpatterns = format_suffix_patterns(urlpatterns)
