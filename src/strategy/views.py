from django.shortcuts import render

# Create your views here.



def status(r):
    return render(r, "strategy/status.html")