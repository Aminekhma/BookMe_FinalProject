from django.core.management.base import BaseCommand, CommandError
from mygutenberg.serializers import listOFBooksSerializer,BookIndexSerializer
from mygutenberg.models import listOFBooks,BookIndex
from mygutenberg.utils import getWordsWithOcc
from mygutenberg.config import number_of_book

from mytig.config import booksUrl
import requests
import time

class Command(BaseCommand):
    help = 'Refresh the list of products which are on sale.'

    def handle(self, *args, **options):
        self.stdout.write('['+time.ctime()+'] Refreshing data...')
        
        listOFBooks.objects.all().delete()
        BookIndex.objects.all().delete()

        i = 0
        page = 1
        map_book_wordOcc = {}

        while (i <= number_of_book):
                            
            response = requests.get(booksUrl+'/books?mime_type=text&page='+str(page))
            print(booksUrl+'/books?mime_type=text&page='+str(page))
            
            jsondata = response.json()
            data = jsondata['results']
            page = page + 1


            for book in data:
                # print(i,book['id'])
                
                if i == number_of_book:
                    i = i +1
                    break
                

                # print("----------------------------------------------------------------------------------")
                # print(books['formats']['image/jpeg'])
                # print("----------------------------------------------------------------------------------")
                try:
                    url_text = book['formats']["text/plain; charset=utf-8"]
                    url_text = url_text.replace(".zip", ".txt")
                    auteur = ('None' if len(book['authors']) == 0 else book['authors'][0]['name'])
                    # book_html = requests.get(url_text).text
                    text_response = (book['title']) + " ".join(book['subjects'])



                except:
                    continue
                serializer = listOFBooksSerializer(data={
                        "id": book['id'],
                        "title": book['title'],
                        "author": auteur,
                        "language": book['languages'][0], 
                        "imageBook":book['formats']['image/jpeg'],
                        "text" : text_response
                        
                })
                if serializer.is_valid():
                    print(i)
                    i = i + 1
                    serializer.save()
                    self.stdout.write(self.style.SUCCESS('['+time.ctime()+'] Successfully added product id="%s"' % book['id']))

                    # book_text = []
                        
  
                    # wordsOcc = getWordsWithOcc(text_response, book['languages'][0])
                    wordsOcc = getWordsWithOcc(text_response, book['languages'][0])

                    dictOcc = dict(wordsOcc)
                    
                    # saveTmpWords(wordsOcc)
                    # print(dict(wordsOcc))
                    # dataIndex = getListIndexBook(wordsOcc, book['id'])
                    # print(dataIndex)

                    serializerIndex = BookIndexSerializer(data={
                                                "id": book['id'],
                                                "title":book['title'],
                                                "wordOcc": str(dictOcc)
                                            })
                    if serializerIndex.is_valid():
                        # map_book_wordOcc[(book['id'])] = wordsOcc
                        
                        serializerIndex.save()
            

            
        self.stdout.write('['+time.ctime()+'] Data refresh terminated.')


            
