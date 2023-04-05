from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary
# Create your models here.
class Post_Model(models.Model):
    class Meta (object):
        db_table="post"
    
    name = models.CharField("Name", max_length=100, null= False, blank= False )
    
    created_at = models.DateTimeField("created DateTime",auto_now=True, blank=True) 
    
    body = models.CharField("body",max_length=500, null=False,blank=False)
    
    image = CloudinaryField("image", blank=True, db_index=True)
    
    likes = models.PositiveIntegerField ("likes", default= 0, null=True, blank=True)
    
    
    def __str__(self):
         return(self.name)