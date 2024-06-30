from django.db import models

class Banner(models.Model):
    title=models.CharField(max_length=255)
    detail=models.TextField()
    background_img=models.ImageField()
    
    def __str__(self):
        return self.title 


class About(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField
    detail=models.TextField()
    
    def __str__(self):
        return f"({self.detail})" 



class Creative_work(models.Model):
    title = models.CharField(max_length=255)
    img = models.FileField()
    detail = models.TextField()
    
    def __str__(self):
        return f"({self.img})" 





    