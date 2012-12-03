from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render_to_response, render
from django.template.defaulttags import csrf_token

def depan(request):
	form = UserCreationForm()
	return render(request, 'umum/depan.jade', {'form':form, })
