from django.shortcuts import render

def home(req):
    return render(req,"temp1.html",{})