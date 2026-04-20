from django.shortcuts import render, redirect

#render: mostrar uma página
#redirect: quer ir para outra URL

def splash_page(request):
    return render(request, 'splash/splash.html')