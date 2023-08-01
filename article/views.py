from django.shortcuts import render,HttpResponse,redirect
from  django.contrib import messages
from .articleform import AddArticleForm
from  article.models import  Article
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# Create your views here.

#require_http_methods bizim kullanıcı girişi yapmdan girdirmicemiz sayfalara koyuyoruz.



def index(request):
    return render(request,"index.html")

#MYabout

@login_required(login_url="user:login")
def About(request):
    return render(request,"about.html") #html sayfasını çağırdık
# detail page

@login_required(login_url="user:login")
def Makaleler(request):

    return render(request,"article.html")
@login_required(login_url="user:login")
def Dashboard(request):
    articles =Article.objects.filter(author =request.user)  # burda sadece şuanki kullanıcı olsun demek istedk

    context= {

        "articles":articles
    }

    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def AddArticle(request):
    form = AddArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article =form.save(commit=False)  # burda direk kaydetme dedikk kayıt işini biz sonlandırdık

        article.author=request.user
        messages.success(request,"Article saved.")
        article.save()
        return redirect("index")
    #burda redirct de kullanaraırız direk yazdığımız fonksiyona götürür bizi ama
    #render de kullandıgımızda direk tml sayfasının çevirir



    return render(request, "addarticle.html",{"form":form}) #burda contexti dışarda oluşturmadan yaptık.
@login_required(login_url="user:login")
def Delete(request,id):
    articles = Article.objects.get(id=id)
    articles.delete()

    messages.success(request,"Article deleted")

    return render(request,"index.html")
@login_required(login_url="user:login")
def Detail(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        article = None

    context = {
        "article": article
    }

    return render(request, "detail.html", context)
@login_required(login_url="user:login")
def UpDate(request, id):
    article = get_object_or_404(Article, id=id)
    forms = AddArticleForm(request.POST or None, request.FILES or None, instance=article)  # Mevcut makale örneğini form'a geçiyoruz.

    if request.method == 'POST':
        if forms.is_valid():
            article = forms.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Article Update.")
            return redirect("index")

    return render(request, "Update.html", {"forms": forms})

def Makaleler(request):
    keyword =request.GET.get("keyword")
    if keyword :
        article=Article.objects.filter(title__contains=keyword)  #biz burda başlığın içinde ieriyormu diye bakıyoruz
        context={
            "article":article
        }
        return render(request,"article.html",context)

    article = Article.objects.all()

    context={
        "article":article
    }
    return render(request,"article.html",context)

#Eğer if koşuluna girmezse tüm articelları çekip işlemimize devam etmiş olucaz


