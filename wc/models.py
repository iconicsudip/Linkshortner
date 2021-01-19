from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class shorturl(models.Model):
    original_url = models.URLField(max_length=200,blank=False)
    short_url = models.CharField(max_length=8,blank=False,null=True)
    clicks = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    url_id = models.IntegerField(default=0)
    total_user = models.IntegerField(default=56800235584)
    def __str__(self):
        return str(self.user)

class notuserurl(models.Model):
    original_url = models.URLField(max_length=200,blank=False)
    short_url = models.CharField(max_length=8,blank=False,null=False)
    total_notuser = models.IntegerField(default=56800235584)
    
    