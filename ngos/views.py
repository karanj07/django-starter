from django.shortcuts import render
from .forms import SchoolForm, SchoolModelForm
from .models import School
from django.views import View
from django.contrib import messages #import messages

from django.core.mail import send_mail
from django.conf import settings

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

            mail_response = send_mail('New School Form',
            'This is some test school message', 
            settings.EMAIL_HOST_USER,
            ['karanj89@gmail.com'], 
            fail_silently=False)
            if mail_response == 1:
                messages.success(request, 'Mail sent successfully.')

            messages.success(request, 'Request added successfully.')
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

        return render(request, "schools/create.html", context)



def schoolDetail(request, pk):
    obj = School.objects.get(pk=pk)

    return render(request, "schools/single.html", {'school':obj})

