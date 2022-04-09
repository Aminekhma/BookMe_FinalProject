from django.db import models

# Create your models here.
class listOFBooks(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    author = models.CharField(max_length=150)
    language = models.CharField(max_length=5, default="")
    title = models.CharField(max_length=255, blank=False)
    imageBook = models.CharField(max_length=355,default="")
    text = models.TextField(default="")
    crank = models.FloatField(default="0.0")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'id'], name='unique')
        ]
        ordering = ['title']
        
class BookIndex(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    title = models.CharField(max_length=50000000, default="")
    wordOcc = models.CharField(max_length=50000000, default="")

    class Meta:
        ordering = ['id','title','wordOcc']
        
        
class BookGraphJaccard(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    neightbors = models.CharField(max_length=50000000, default="")

    class Meta:
        ordering = ['id','neightbors']