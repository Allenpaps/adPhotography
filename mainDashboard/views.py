from django.shortcuts import render

def baseView(request):
    return render(request, 'core/main.html')
