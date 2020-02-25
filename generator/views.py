from django.shortcuts import render
import random

def home(request):
	return render(request, 'generator/home.html', {})


def password(request):

	if request.method == "POST":

		characters = list('abcdefghiklmnopqrstuvwxyz')

		if request.POST.get('uppercase'):
			characters.extend(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'))
		if request.POST.get('numbers'):
			characters.extend(list('0123456789'))
		if request.POST.get('special'):
			characters.extend(list('@$#!^%&*()'))
			
		length = int(request.POST.get('length'))
		pword = ""
		for i in range(length):
			pword += random.choice(characters)

		return render(request, 'generator/password.html', {'password':pword})
	else:
		return render(request, 'generator/password.html',{} )