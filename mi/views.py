from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def rohith(request):
    return render(request,'rohith.html')


def sky(request):
    return HttpResponse('<h1><marquee>he is the best 360 degrees batsman</h1></marquee>')