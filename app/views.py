from django.shortcuts import render

# Create your views here.
def second(request):
    d={'a':10,'b':20,'c':30}
    return render(request,'second.html',d)