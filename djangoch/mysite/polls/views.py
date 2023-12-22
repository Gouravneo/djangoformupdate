from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Studyprogram
from .form import StudentForm



def home(request):
    all_members=Studyprogram.objects.all
    return render (request,'home.html',{'all':all_members})

def join(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save( )
            print("Form Saved")
        return redirect('home')
    else:
        return render(request,'join.html',{})    



def index(request):
    return HttpResponse('Hello World Gourav')
def heybro(request):
    return HttpResponse('HEY BRO')
def hi(request):
    return HttpResponse("Hey hi iam gourav")

