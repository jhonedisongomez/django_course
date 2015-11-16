from django.conf.urls import patterns, include, url
from .views import IndexView

urlpatterns = patterns('',
    url(r'^$' ,IndexView.as_view()),
   # url(r'^index$' ,Index2.as_view() ),
   # url(r'^index/', Index.as_view()),
   	#url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio/index.html'},name='login'),
	#url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),
)