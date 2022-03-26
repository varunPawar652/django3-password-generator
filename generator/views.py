from django.shortcuts import render
from django.http import HttpResponse
import random
import string



def A1(request):
    return HttpResponse("Hey Jadugar aad hello")
def A2(request):

    characters = string.ascii_lowercase

    length = int(request.GET.get('length',12))
    if request.GET.get('UpperCase'):
        characters += string.ascii_uppercase
    if request.GET.get('Number'):
        characters += string.digits
    if request.GET.get('Special'):
        characters += string.punctuation
    generated_password = ""

    characters = list(characters)
    for x in range (length):
        generated_password += random.choice(characters)


    return render(request,'password.html',{'password':generated_password})
def password(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
