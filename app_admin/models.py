from django.db import models

# Create your models here.
class   RegisterTb(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SignupTb(models.Model):
    user_name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class CategoryTb(models.Model):
    category_name=models.CharField(max_length=20) 
    def __str__(self):
        return self.category_name

class ShowTb(models.Model):
    title=models.CharField(max_length=50)
    poster=models.FileField()    
    category=models.ForeignKey(CategoryTb,on_delete=models.CASCADE)
    genre=models.CharField(max_length=50)
    released=models.CharField(max_length=20)
    language=models.CharField(max_length=20)
    rating=models.CharField(max_length=20)
    director=models.CharField(max_length=20)
    story=models.CharField(max_length=200)

    def __str__(self):
        return self.title