from django.core.management.base import BaseCommand, CommandError
from mygutenberg.serializers import listOFBooksSerializer,BookGraphJaccardSerializer
from mygutenberg.models import listOFBooks,BookIndex,BookGraphJaccard
from mygutenberg.utils import distance_jaccard
from mygutenberg.config import number_of_book

from mytig.config import booksUrl
import requests
import time
import ast

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')

        
        
        BookGraphJaccard.objects.all().delete()
        sum_distance = 0
        SEUIL = 0.65
        cpt = 0
        books = []

        for book1 in BookIndex.objects.all():

            # print("FOR BOOK :"+str(book1.title))
            for book2 in BookIndex.objects.all():
                if book1.id != book2.id:
                    # print("         DISTANCE WITH ====> "+str(book2.title))
                    d1 = ast.literal_eval(book1.wordOcc)
                    d2 = ast.literal_eval(book2.wordOcc)
                    res_distance = distance_jaccard(d1, d2)
                    
                    if res_distance < SEUIL:
                        books.append(book2.id)
                    
                    sum_distance += res_distance
                    # print(res_distance)

            #
            cpt+=1
            print(cpt)
            serializer = BookGraphJaccardSerializer(data={
                        "id": book1.id,
                        "neightbors": str(books)    
                })
            if serializer.is_valid():
                serializer.save()
                self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added Graph Jaccard for '+ str(book1.title)))
            crank = (number_of_book - 1) / sum_distance
            
            book = listOFBooks.objects.get(id=book1.id)
            book.crank = crank
            book.save()
            sum = 0
            books = []
            sum_distance = 0


    


       

            
