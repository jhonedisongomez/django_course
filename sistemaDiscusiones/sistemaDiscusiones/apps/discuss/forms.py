# -*- encoding: utf-8 -*-
from django import forms
from .models import Question

class CreateQuestionForm(forms.ModelForm):

	title = forms.CharField(widget = forms.TextInput(attrs={
			'class' : 'class-control',
			'placeholder' : 'título'


		}))

	description = forms.CharField(widget = forms.Textarea(attrs={
			'class' : 'class-control',
			'placeholder' : 'Contenido',
			'rows' : 4


		}))	

	class Meta:
		model =  Question