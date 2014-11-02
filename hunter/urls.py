from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hunter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hunter.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
        }),
)