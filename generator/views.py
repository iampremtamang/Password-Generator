from django.shortcuts import render


def home(request):
	return render(request, 'generator/home.html', {})


def password(request):
	return render(request, 'generator/password.html', {})