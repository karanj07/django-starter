from django.shortcuts import render

from .models import School
# Create your views here.


def index(request):
    #dests = School.objects.all()
    return render(request, "schools/all.html", {'schools':School.objects.all()})


def create(request):
    if (request.method== 'POST'):
        email = request.POST['email']
        pwd = request.POST['password']
        if(len(pwd)  < 5):
            messages.info(request, "password is too short")
        print(email)
        return render(request, "schools/create.html")
    else:
        return render(request, "schools/create.html")


def schoolDetail(request, pk):
    obj = School.objects.get(pk=pk)

    return render(request, "schools/single.html", {'school':obj})

