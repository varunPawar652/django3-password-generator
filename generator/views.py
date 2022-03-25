from django.shortcuts import render
from django.http import HttpResponse
import random

def A1(request):
    return HttpResponse("Hey Jadugar aad hello")
def A2(request):

    characters = "abcdefghijklmnopqrstuvwxyz"

    length = int(request.GET.get('length',12))
    if request.GET.get('UpperCase'):
        characters += characters.upper()
    if request.GET.get('Number'):
        characters += '0123456789'
    if request.GET.get('Special'):
        characters += "`!~@#$%^&*()_+}{\":<>?/.,;'\][=-]"
    generated_password = ""

    characters = list(characters)
    for x in range (length):
        generated_password += random.choice(characters)


    return render(request,'password.html',{'password':generated_password})
def password(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
