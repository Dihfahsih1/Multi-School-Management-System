from django.shortcuts import render, HttpResponse
def home(request):
    return render(request, 'accounts/home.html')

# Create your views here.
