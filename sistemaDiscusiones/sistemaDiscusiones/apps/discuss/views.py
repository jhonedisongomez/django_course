from django.shortcuts import render
from .models import Question, Tag
from braces.views import LoginRequiredMixin

from django.views.generic import ListView, CreateView
from .forms import CreateQuestionForm


class QuestionListView(ListView):
	model = Question
	context_object_name = 'questions'

	def get_context_data(self, **kwargs):
		context = super(QuestionListView, self).get_context_data(**kwargs)
		context['tags'] = Tag.objects.all()
		return context


class QuestionCreateView(LoginRequiredMixin,CreateView):

	model = Question
	form_class = CreateQuestionForm
	success_url = '/'
	login_url = '/'

	def form_valid(self, form):
		#print "valido"
		form.instance.user = self.request.user
		return super(QuestionCreateView, self).form_valid(form)

	
	def form_invalid(self, form):
		#print "invalido"
		return super(QuestionCreateView, self).form_invalid(form)

