from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home.views import IndexView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView.as_view(), name='index'),
    # url(r'^startdust_website/', include('startdust_website.foo.urls')),

    #(r'^panel/projects/add/', )
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^auth/', include('registration.auth_urls')),
)

urlpatterns += staticfiles_urlpatterns()
