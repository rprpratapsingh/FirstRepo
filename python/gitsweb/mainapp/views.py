from django.shortcuts import render
from django.http import HttpResponse
from . import connection as pydb

def home(request):
    return render(request,"college.html",{})

def log(request):
    return render(request,"index.html",{})

def test(request):
    txt = request.GET['lo']
    return render(request,"index.html",{})

def login(request):
    username = request.POST['user']
    password = request.POST['pass']
    query = "select * from signup where email='{0}' and phone='{1}'".format(username,password)
    data = pydb.fetch(query)
    if len(data)==0:
        return HttpResponse("<h1>wrong ID or Password</h1>")
    else:
        return render(request,"college.html",{"name": username})


def signup(request):
    return render(request,"signup.html",{})

def save(request):
    name = request.POST['name']
    date = request.POST['dob']
    gender = request.POST['gender']
    email = request.POST['email']
    phone  = request.POST['phone']
    insert1 = "INSERT INTO signup VALUES('{0}', '{1}', '{2}', '{3}', {4})".format(name,date,gender,email,phone)
    pydb.exec(insert1)
    return render(request,"index.html",{})