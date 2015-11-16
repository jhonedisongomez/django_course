from django.conf.urls import patterns, include, url
from .views import QuestionListView, QuestionCreateView	

urlpatterns = patterns('',
    url(r'preguntas/$', QuestionListView.as_view(), name='questions'),
    url(r'preguntar/$', QuestionCreateView.as_view(), name='create_question'),
   
)