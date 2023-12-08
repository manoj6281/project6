from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')


def jadeja(request):
    return HttpResponse('<h1><marquee>he is the best spin bowler</h1></marquee>')