from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Create your views here.
def virat(request):
    return render(request,'virat.html')


def siraj(request):
    return HttpResponse('<h1><marquee>he is the best bowler india</h1></marquee>')