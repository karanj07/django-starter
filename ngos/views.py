from django.shortcuts import render
from .forms import SchoolForm, SchoolModelForm
from .models import School
from django.views import View
# Create your views here.


def index(request):
    #dests = School.objects.all()
    return render(request, "schools/all.html", {'schools':School.objects.all()})


def create(request):
    context={'form':SchoolModelForm}
    if (request.method== 'POST'):
        email = request.POST['email']
        pwd = request.POST['password']
        if(len(pwd)  < 5):
            messages.info(request, "password is too short")
        print(email)
        return render(request, "schools/create.html", context)
    else:
        return render(request, "schools/create.html", context)

class CreateSchool(View):
    def get(self, request):
        context={'form':SchoolModelForm}
        return render(request, "schools/create.html", context)

    def post(self, request):
        context={'form':SchoolModelForm}

        form = SchoolModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass

        return render(request, "schools/create.html", context)



def schoolDetail(request, pk):
    obj = School.objects.get(pk=pk)

    return render(request, "schools/single.html", {'school':obj})

