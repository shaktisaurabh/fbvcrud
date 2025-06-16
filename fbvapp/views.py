from django.shortcuts import render,redirect
from .models import student 
from fbvapp.forms import studentform
# Create your views here.
def getstudents(request):
    students = student.objects.all()
    return render(request, "fbvapp/index.html",{"students": students})

def createstudent(request):
    form=studentform()
    if request.method=="POST":
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,"fbvapp/create.html",{"form":form}) 

def deletestudent(request,id):
    student_obj=student.objects.get(id=id)
    student_obj.delete()
    return redirect('/') 

def updatestudent(request,id):
    student_obj=student.objects.get(id=id)
    form=studentform(instance=student_obj)
    if request.method=="POST":
        form=studentform(request.POST,instance=student_obj)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,"fbvapp/update.html",{"form":form})
    
