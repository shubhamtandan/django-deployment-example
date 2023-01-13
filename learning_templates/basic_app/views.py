from django.shortcuts import render

# Create your views here.

def index(request):
    c = {'text':'hello world','number':100}
    c = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html',c)

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
