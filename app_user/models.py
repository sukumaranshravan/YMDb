from django.db import models

# Create your models here.
class ReviewTb(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    date=models.CharField(max_length=20,default=0)
    time=models.CharField(max_length=20,default=0)
    user_id=models.ForeignKey('app_admin.RegisterTb',on_delete=models.CASCADE)
    poster=models.FileField()

class WatchlistTb(models.Model):
    show_id=models.ForeignKey('app_admin.ShowTb',on_delete=models.CASCADE)
    user_id=models.ForeignKey('app_admin.RegisterTb',on_delete=models.CASCADE)


