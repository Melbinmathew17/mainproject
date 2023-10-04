from django.shortcuts import render,redirect
from myapp.models import departmentdb,doctorsdb,service_db
from webapp.models import userlogin,appoinmentdb,messagedb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def indexpage(request):
    return render(request,"index.html")

def departmentpage(request):
    return render(request,"adddepartment.html")

def savedepartment(request):
    if request.method=="POST":
        n=request.POST.get('Department')
        d=request.POST.get('Describe')
        img=request.FILES['Image']
        obj=departmentdb(Department=n,Describe=d,Image=img)
        obj.save()
        return redirect(departmentpage)

def displaydepartment(request):
    data= departmentdb.objects.all()
    return render(request,"displaydepartment.html",{'data':data})

def editdepartment(request,dataid):
    data=departmentdb.objects.get(id=dataid)
    return render(request,"editdepartment.html",{'data':data})

def updatedepartment(request,dataid):
    if request.method=="POST":
        n = request.POST.get('Department')
        d = request.POST.get('Describe')
        try:
            img=request.FILES['Image']
            fs= FileSystemStorage()
            file= fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=departmentdb.objects.get(id=dataid).Image
        departmentdb.objects.filter(id=dataid).update(Department=n,Describe=d,Image=file)
        return redirect(displaydepartment)

def deletedepartment(request,dataid):
    data=departmentdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydepartment)

def doctorspage(request):
    data=departmentdb.objects.all()
    return render(request,"adddoctors.html",{'data':data})

def savedoctor(request):
    if request.method=="POST":
        c=request.POST.get('Departmentname')
        p=request.POST.get('Name')
        d=request.POST.get('Qualification')
        e=request.POST.get('About')
        im=request.FILES['image']
        obj=doctorsdb(Departmentname=c,Name=p,Qualification=d,About=e,image=im)
        obj.save()
        messages.success(request,"Doctor Saved Successfully")
        return redirect(doctorspage)


def displaydoctors(request):
    data = doctorsdb.objects.all()
    return render(request, "displaydoctors.html",{'data': data})

def editdoctor(request,dataid):
    data=departmentdb.objects.all()
    products=doctorsdb.objects.get(id=dataid)
    return render(request,"editdoctors.html",{'data':data, 'products':products})

def updatedoctor(request,dataid):
    if request.method=="POST":
        c = request.POST.get('Departmentname')
        p = request.POST.get('Name')
        d = request.POST.get('Qualification')
        e = request.POST.get('About')
        try:
            im=request.FILES['image']
            fs= FileSystemStorage()
            file= fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=doctorsdb.objects.get(id=dataid).image
        doctorsdb.objects.filter(id=dataid).update(Departmentname=c,Name=p,Qualification=d,About=e,image=file)
        messages.success(request,"Data Updated")
        return redirect(displaydoctors)

def deletedoctor(request,dataid):
    data=doctorsdb.objects.filter(id=dataid)
    data.delete()
    messages.error(request,"Data Deleted")
    return redirect(displaydoctors)

def adminpage(request):
    return render(request,"adminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(adminpage)

    else:
        return redirect(adminpage)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminpage)

def appoinment_page(request):
    data=appoinmentdb.objects.all()
    return render(request,"displayappoinment.html",{'data':data})

def messagepage(request):
    data=messagedb.objects.all()
    return render(request,"displaymessage.html",{'data':data})

def service_page(request):
    data=service_db.objects.all()
    return render(request,"addservice.html",{'data':data})

def saveservice(request):
    if request.method=="POST":
        c=request.POST.get('Service')
        p=request.POST.get('Describe')
        im=request.FILES['Image']
        obj=service_db(Service=c,Describe=p,Image=im)
        obj.save()
        return redirect(service_page)

def displayservice(request):
    data = service_db.objects.all()
    return render(request, "displayservice.html",{'data': data})


