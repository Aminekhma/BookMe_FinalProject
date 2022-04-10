import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl
from mytig.config import booksUrl
from django.http import Http404, HttpResponse
import json
from subprocess import Popen, PIPE, run,call
import ast

from mygutenberg.models import BookIndex,BookGraphJaccard
from mygutenberg.models import listOFBooks

from mygutenberg.serializers import listOFBooksSerializer
from mygutenberg.serializers import BookIndexSerializer

from django.http import Http404
from django.http import JsonResponse


# Create your views here.
class listBooks(APIView):
    def get(self, request, format=None):
        response = requests.get(booksUrl+'books/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class detailBook(APIView):
    def get_object(self, id):
        try:
            return listOFBooks.objects.get(id=id)
        except listOFBooks.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        livre = self.get_object(pk)
        jsondata = listOFBooksSerializer(livre)
        print(jsondata)

        return handleResponse(status="OK", result=jsondata.data, message="Voici le livre", codeStatus=200)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


class AvailableProducts(APIView):
    def get(self, request, format=None):
        # res=[]
        # for prod in ProduitEnPromotion.objects.all():
        #     serializer = ProduitEnPromotionSerializer(prod)
        #     response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        #     jsondata = response.json()
        #     res.append(jsondata)
        res=[]
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        
        for i in jsondata:
            if i['availability'] == True:
                res.append(i)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class AvailableProductDetail(APIView):

    def get(self, request, pk, format=None):
        # prod = self.get_object(pk)
        # serializer = ProduitEnPromotionSerializer(prod)
        # response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        # jsondata = response.json()
        res=[]
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        for i in jsondata:
            if i['availability'] == True and i['id']==pk :
                res.append(i)
        return JsonResponse(res, safe=False)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


def handleResponse(status, result, message, codeStatus):
    response_data = {}
    response_data['status'] = status
    response_data['message'] = message
    response_data['result'] = result

    return HttpResponse(json.dumps(response_data), content_type="application/json", status=codeStatus)

#################################################################################################################################################
#################################################################################################################################################
class SearchAPI(APIView):
    def get_object(self, id):
        try:
            return listOFBooks.objects.get(id=id)
        except listOFBooks.DoesNotExist:
            raise Http404
    def get(self, request,word, format=None):
        res=[]
        books = []
        books_id = []
        neightbors = []
        neightbors_final = []
        result_withneightbors = {}
        for book in BookIndex.objects.all():

            d = ast.literal_eval(book.wordOcc)
            for key, value in  d.items():
                if key == word or key == word.lower():
                    query = listOFBooks.objects.filter(id=book.id) 
                    query.update(occurence=value)
                    books_id.append(book.id)
                    books += query
                    bookJacc = BookGraphJaccard.objects.get(id=book.id)
                    neightbors += ast.literal_eval(bookJacc.neightbors)

        books_id = set(books_id)
        neightbors = set(neightbors)
        neightbors = neightbors - books_id
        for neigh in neightbors:
            queryn = listOFBooks.objects.filter(id=neigh)
            queryn.update(occurence=0)
            neightbors_final += queryn

        jsondataBook = (listOFBooksSerializer(books, many=True)).data
        jsondataBookneigh = (listOFBooksSerializer(neightbors_final, many=True)).data

        result_withneightbors["books"] = jsondataBook
        result_withneightbors["neightboors"] = jsondataBookneigh
        
        return JsonResponse(result_withneightbors, safe=False)

#################################################################################################################################################
#################################################################################################################################################
class SearchRegexAPI(APIView):
    
    def get_object(self, id):
        try:
            return listOFBooks.objects.get(id=id)
        except listOFBooks.DoesNotExist:
            raise Http404
        
    def get(self, request,word, format=None):
        res=[]
        for book in listOFBooks.objects.all():
            neightbors = []
            result_withneightbors = {}
            f = open("./text.txt", "w", encoding="utf-8")
            f.truncate()
            f.write(book.text)
            f.close()
            command = ["java", "-jar", "./egrep.jar", word,"./text.txt"]
            run_command = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            result = run_command.stdout
            print(result)
            if int(result) >0:
                bookJacc = BookGraphJaccard.objects.get(id=book.id)
                res.append(book.title)
                neightbors += ast.literal_eval(bookJacc.neightbors)
                
            result_withneightbors["books"] = res
            result_withneightbors["neightboors"] = neightbors
        
        return JsonResponse(result_withneightbors, safe=False)