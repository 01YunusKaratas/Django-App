from django import forms
#This form use for login.form
# django has got form

class LogınForm(forms.Form):
    username = forms.CharField(label="USERNAME") #biz yazı alanı olması için djangoda charfield kullanıyoruz.
    password = forms.CharField(label="PASSWORD",widget=forms.PasswordInput)
#Biz bu classta clean yapmadık fakat,zaten clean methodu içinde kendi çalışıyor yapmayınca clean methodu aslında biz aşşagıda override etmiş oluyoruz.

    

class RegısterForm(forms.Form):

    username=forms.CharField(max_length=50,min_length=3,label="USERNAME:")
    password=forms.CharField(max_length=50,min_length=5,label="PASSWORD:",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=50,min_length=5,label="PASSWORD/AGAIN:",widget=forms.PasswordInput)
    #widget özelliği

    #form submit eedilmeden önce biz burda bilgilerimizi almış oluyoruz
    def clean(self):  #biz burda ovveride yapmış oluyoruz
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm =self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError(message="Lütfen bilgileri kontrol ediniz")


        else:
            #yukarıda oluşturdugumuz bilgileri burda sözlük içinde tutup diger sayfalarda kullandık
            context = {
                #bizim bunu burda yapma şeklimiz contexti registerhtmlin içine gönderme
                "username":username,
                "password":password,
                "confirm":confirm,
            }
            return context
