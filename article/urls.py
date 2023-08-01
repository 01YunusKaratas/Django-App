from django.contrib import admin
from django.urls import path
from . import views

app_name = "article" #bunu redirct işlemi yaparken lazım olucak diye yazdık

urlpatterns = [
    path('about/',views.About,name="about"),
    path('article/addarticle/',views.AddArticle),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('karataş/',views.About),
    path('delete/<int:id>/',views.Delete,name="delete"),
    # burda id statik bir yapı olduğu için onu unutmamak lazım sürekli değişiyr o
    path('dashboard/<int:id>/',views.Detail,name="detail"),
    path('update/<int:id>/',views.UpDate,name ="update"),
    path('makaleler/',views.Makaleler,name="makaleler"),









]