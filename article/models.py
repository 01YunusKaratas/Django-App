from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    #Buradaki bütün mdouller hazır olarak databaseden alınıyor

    author = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")  #burada Foreign key yaparak auth usera gittik , models.Cascade ile de eğer kullancıı silinirse bilgileri sildik.
    title =models.CharField(max_length=75,verbose_name="Başlık") #makale başlığı
    content =RichTextField()
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Tarih")  # bu makale ne zaman oluşmuş ona bakıyor
    article_image= models.FileField(blank=True,null=True,verbose_name="Image")
    # Yani resim alanı hem boş olabilir hemde dolu olabilir onu demek istiyoruz yukarıda

    def __str__(self):
        return  self.title  #bir print işlevi görüü


