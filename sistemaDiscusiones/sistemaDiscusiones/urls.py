from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^' , include('sistemaDiscusiones.apps.home.urls')),
    url(r'^' , include('sistemaDiscusiones.apps.users.urls',namespace= 'users')),
    url(r'^' , include('sistemaDiscusiones.apps.discuss.urls',namespace= 'discuss')),
)
