from django.shortcuts import render
from django.views.generic import DetailView
from .models import User
from sistemaDiscusiones.apps.discuss.models import Question	
# Create your views here.

class UserDetailView(DetailView):

	model = User
	slug_field = 'username'

	def get_context_data(self, **kwargs):
		context  = super(UserDetailView, self).get_context_data(**kwargs)
		questions = Question.objects.filter(user = context['object']).order_by('created')
		tags = [ question.tag.all() for question in questions ]
		context['ques_tags'] = zip(questions , tags)
		return context