from django.shortcuts import render,HttpResponse,redirect
from .models import Form
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        image=request.FILES.get('image')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        exp=request.POST.get('exp')
        cv=request.FILES.get('cv')
        file=request.FILES.get('file')
        form=Form(name=name,email=email,phone=phone,exp=exp,cv=cv,file=file,image=image)
        form.save()
        return redirect('submitted')
    return render(request,'resume_form.html')

def submitted(request):
    per=Form.objects.all()
    return render(request,'submitted.html',{"data":per})
