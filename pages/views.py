from django.shortcuts import render

# Create your views here.
def home(request):
    ctx = {}
    return render(request, 'pages/home.html', ctx)

def about(request):
    return render(request, 'pages/about.html')
