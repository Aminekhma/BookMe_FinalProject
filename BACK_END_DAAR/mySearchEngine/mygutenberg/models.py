from django.db import models

# Create your models here.
class listOFBooks(models.Model):
    id = models.IntegerField(null=False, primary_key=True)          # id du livre dans la base du site gutenberg
    author = models.CharField(max_length=150)                       # auteur du livre
    language = models.CharField(max_length=5, default="")           # la langue 
    title = models.CharField(max_length=255, blank=False)           # titre du livre
    imageBook = models.CharField(max_length=355,default="")         # Image de la face avant du livre
    text = models.TextField(default="")                             # contenu du livre ou sommaire + titre
    crank = models.FloatField(default="0.0")                        # score du livre pour le classement
    occurence = models.IntegerField(default="0")

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