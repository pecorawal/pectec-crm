from django.shortcuts import render

def homepage(request):
    return render(request,"homepage.html")

def lojas(request):
    return render(request,"lojas.html")

def carrinho(request):
    return render(request,"carrinho.html")

def checkout(request):
    return render(request,"checkout.html")

def minha_conta(request):
    return render(request,"usuario/minhaconta.html")

def login(request):
    return render(request,"usuario/login.html")
