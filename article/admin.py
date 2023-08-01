from django.contrib import admin
from .models import Article  #models sayfasından al articlei

# Register your models here.


@admin.register(Article)  # models sayfasındaki aldığımız article classını kayıtettik.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]  #bunu kullanarak ana ekranda liste içindeki  özelliklerini gösterebiliyoruz.
    list_display_links = ["title","author","created_date"]  #bu kod blogunu kullanarak içeriklere basarak güncelleme sayfasına gidiyoruz.
    list_per_page = 5
    search_fields = ["title"]
    list_filter = ["created_date"]  # bu kod makalenn hangi ügn hangi ayda yapıldıgını gösterir.


    class Meta:  #bize python tarafından söylenen bir sınıf adı.Bunu yaparak model ile Articlei bağdaştırdık.
        model =Article







