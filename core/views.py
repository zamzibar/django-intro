from django.shortcuts import render, HttpResponse

# Create your views here.
def hello1(request):
    return  HttpResponse('<h1>Hello</h1>')

def hello2(request, nome):
    return  HttpResponse('<h1>Hello {}</h1>'.format(nome))

def hello3(request, nome, idade):
    return  HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))