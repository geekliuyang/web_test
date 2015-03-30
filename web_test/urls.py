from django.conf.urls import patterns, include, url
from django.contrib import admin
from books.views import hello, display_meta, search_info, search
from contact.views import contact
from contact.views import thank


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'web_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^meta/$', display_meta),
    url(r'^search_info/$', search_info),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^contact/thanks$', thank)
)
