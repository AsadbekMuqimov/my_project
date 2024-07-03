
from django.shortcuts import render
from . import models


def main(request):
    banner = models.Banner.objects.all()
    about = models.About.objects.all()
    address = models.Address.objects.all()
    if request.method == 'POST':
        f_name = request.POST["f_name"]
        phone = request.POST["Telefon raqam"]
        email = request.POST["Pochta manzilingiz"]
        messege = request.POST["Xabarlaringiz"]
        print(f_name)
        models.Address.objects.create(
            f_name=f_name,
            phone=phone,
            email=email,
            messege=messege,
        )
   
    context ={
        'banners': banner,
        'abouts': about,
        'address': address, 
    }
    return render(request, 'index.html', context)
