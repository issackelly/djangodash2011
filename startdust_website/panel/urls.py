from django.conf.urls.defaults import patterns, include, url
from panel.views import IndexView

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='panel-index'),

    (r'^projects/(?P<id_project>\d+)/$', 'panel.views.show_project'),
    (r'^projects/add/', 'panel.views.add_project'),
)
