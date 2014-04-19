from django.conf.urls import patterns, include, url

from django.contrib import admin
from pastebin.views import HomeView, DetailItemView, AddFormView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pasteproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^paste/$',HomeView.as_view(),name = 'homepage'),
    url(r'^paste/(?P<pk>\d+)/$',DetailItemView.as_view(),name = 'detailitem'),
    url(r'^paste/add/$',AddFormView.as_view(),name = 'addform')
)
