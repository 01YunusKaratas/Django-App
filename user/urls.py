from django.contrib import admin
from django.urls import path,include

from user import views
#BİZ USER dosyaSININ userpy sinde hep sayfaları oluşturup ana urlse çekiyoruz
app_name ="user"


urlpatterns = [
    path('register/',views.Register,name =" register"),
    path('login/',views.Logın,name = "login"),
    path('logout/',views.Logout,name = "logout"),

]
