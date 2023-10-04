from django.shortcuts import render,redirect
from myapp.models import departmentdb,doctorsdb,service_db
from webapp.models import userlogin,appoinmentdb,messagedb
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,"home.html")

def aboutpage(request):
    return render(request,"about.html")

def servicepage(request):
    ser = service_db.objects.all()
    return render(request, "service.html", {'ser': ser})

def contactpage(request):
    return render(request,"contact.html")

def appoinmentpage(request):
    data = departmentdb.objects.all()
    products = doctorsdb.objects.all()
    return render(request,"appoinment.html", { 'department': data, 'doctors': products })

def appoinmentsave(request):
    if request.method == "POST":
        p=request.POST.get('department')
        r=request.POST.get('doctor')
        q=request.POST.get('date')
        u=request.POST.get('time')
        n=request.POST.get('name')
        t=request.POST.get('user')
        w=request.POST.get('phone')
        z=request.POST.get('message')
        obj=appoinmentdb(department=p,doctor=r,date=q,time=u,name=n,user=t,phone=w,message=z)
        obj.save()
        messages.success(request, "Appoinment Fixed")
        return redirect(homepage)



def department_page(request):
    data = departmentdb.objects.all()
    return render(request,"department.html",{'data': data})

def doctorspage(request,catg):
    products=doctorsdb.objects.filter(Departmentname=catg)
    return render(request,"doctors.html",{'products':products})

def loginpage(request):
    return render(request,"login.html")

def userregister(request):
    if request.method=="POST":
        u=request.POST.get('username')
        e=request.POST.get('email')
        p=request.POST.get('password')
        obj=userlogin(username=u,email=e,password=p)
        obj.save()
        return redirect(loginpage)

def userloginn(request):
    if request.method=="POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if userlogin.objects.filter(username=username_r,password=password_r).exists():

            request.session['usernamel'] = username_r
            request.session['passwordl'] = password_r

            return redirect(homepage)
        else:
            return redirect(loginpage)
    return redirect(loginpage)

def userlogout(request):
    del request.session['usernamel']
    del request.session['passwordl']
    return redirect(homepage)

def singledoctor(request,dataid):
    data=doctorsdb.objects.get(id=dataid)
    return render(request,"singledoctor.html",{'data':data})

def messagesave(request):
    if request.method == "POST":
        p=request.POST.get('name')
        r=request.POST.get('email')
        q=request.POST.get('subject')
        u=request.POST.get('phone')
        z=request.POST.get('message')
        obj=messagedb(name=p,email=r,subject=q,phone=u,message=z)
        obj.save()
        messages.success(request, "Message Send")
        return redirect(homepage)
