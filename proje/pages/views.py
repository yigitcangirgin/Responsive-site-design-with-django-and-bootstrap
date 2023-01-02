from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request , 'pages/index.html')

def girisyap(request):
    return render(request , 'pages/girisyap.html')

def kayitol(request):
    return render(request , 'pages/kayitol.html')

def muzik(request):
    return render(request , 'pages/muzik.html')

def oyunlar(request):
    return render(request , 'pages/oyunlar.html')

def uncharted2(request):
    return render(request , 'pages/uncharted2.html')

def uncharted3(request):
    return render(request , 'pages/uncharted3.html')

def uncharted4(request):
    return render(request , 'pages/uncharted4.html')

def uncharted5(request):
    return render(request , 'pages/uncharted5.html')