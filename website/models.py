from django.db import models

class Banner(models.Model):
    title=models.CharField(max_length=255)
    detail=models.TextField()
    background_img=models.ImageField()
    
    def __str__(self):
        return self.title 


class About(models.Model):
    title=models.CharField(max_length=255)
    img=models.ImageField()
    detail=models.TextField()
    
    def __str__(self):
        return f"({self.detail})" 



class Address(models.Model):
    f_name  = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    messege = models.TextField()
   
    
    def __str__(self):
        return f"({self.f_name}, {self.phone}, {self.email}, {self.messege})"
    

    
    

    




    