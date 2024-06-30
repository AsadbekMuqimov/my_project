
from django.shortcuts import render
from . import models
def main(request):
    banner = models.Banner.objects.all()
    about = models.About.objects.all()
    creative_works = models.Creative_work.objects.all()
    context ={
        'banners': banner,
        'abouts': about,
        'creative_works': creative_works
    }
    return render(request, 'index.html', context)
