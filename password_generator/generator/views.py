from django.shortcuts import render
import random
import string


def home(request):
    return render(request, "generator/home.html")


def about(request):
    return render(request, "generator/about.html")


def your_password(request):

    thepassword = ''

    characters = list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        characters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        characters.extend(list(string.punctuation))
    if request.GET.get('numbers'):
        characters.extend(list(string.digits))

    length = int(request.GET.get('length'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/your_password.html", {'password': thepassword})
