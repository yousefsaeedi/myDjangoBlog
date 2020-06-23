from django.shortcuts import render, HttpResponse

def about(request):
    # return HttpResponse('Hi')
    return render(request, 'about.html')

def home(request):
    # return HttpResponse('This Is HomePage')
    return render(request, 'Home.html')
