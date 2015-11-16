from django.conf.urls import patterns, include, url
from .views import UserDetailView

urlpatterns = patterns('',

	url(r'usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),


)