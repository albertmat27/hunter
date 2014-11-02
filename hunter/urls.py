from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hunter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hunter.views.home', name='home'),
    url(r'^login/$', 'SignIn.views.login_user'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/register/$', 'SignIn.views.register'),
    url(r'^accounts/register/success/$', 'hunter.views.home'),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
        }),
)

(r"^item_action/(done|delete|onhold)/(\d*)/$", "item_action"),