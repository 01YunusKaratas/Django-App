from django.shortcuts import render,redirect
from .forms import RegısterForm,LogınForm

from django.contrib.auth.models import User  #bunu obje oluşturmak için kullanıcaz
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def Register(request):



        form =RegısterForm(request.POST or None)  # burda if else ile kontrol yerine or none ekledik ve olay bitti.

        if form.is_valid():  #aslında biz bu kod bloğunu cağırdığımızda clean classını çağırmış oluyoruz.
            username =form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # obje oluştuurup o objeyi kaydettik.
            newuser =User(username=username)
            newuser.set_password(password)
            newuser.save()

            login(request,newuser)
            messages.success(request , "Registration succesfull...")

            return redirect("index")
        context = {

            "form": form

        }
        return render(request, "register.html", context)




def Logın(request):
    form =LogınForm(request.POST or None)

    context = { #bunu yapma sebebimz template göndermek

        "form":form

    }

    if form.is_valid():# form dogruysa true doner ve değerleri tutar
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(password=password,username=username) #burda doğru oldugu için veritabanındakiyle kontrol ediyoruz.

        login(request,user) #burda ise giriş izni veriyoruz.

        if user is None:
            messages.info(request,"Please check at username and password ")
            return render(request,"login.html",context)
        # yukarıda hatalıysa döngüye gircek değilse devam edcek
        #aşşagıda kullalncıı giriş yapıldı
        messages.success(request,"User login successfull")
        return render(request,"index.html")

    return render(request,"login.html",context)




    return  render(request,"login.html")

@login_required(login_url="user:login")
def Logout(request):

    logout(request)
    messages.success(request,"Signed out of the system.") #messajı yazarken. yanındakini yazmayı unutma


    return render(request,"index.html")





