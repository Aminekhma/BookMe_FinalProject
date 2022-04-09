import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from mytig.config import baseUrl

# Create your views here.
class RedirectionListeDeProduits(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'products/')
        jsondata = response.json()
        return Response(jsondata)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class RedirectionDetailProduit(APIView):
    def get(self, request, pk, format=None):
        try:
            response = requests.get(baseUrl+'product/'+str(pk)+'/')
            jsondata = response.json()
            return Response(jsondata)
        except:
            raise Http404
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"



from mytig.models import ProduitEnPromotion
from mytig.serializers import ProduitEnPromotionSerializer
from mytig.models import ShipPoints
from mytig.serializers import ShipPointSerializer
from django.http import Http404
from django.http import JsonResponse

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

class PromoList(APIView):
    def get(self, request, format=None):
        res=[]
        for prod in ProduitEnPromotion.objects.all():
            serializer = ProduitEnPromotionSerializer(prod)
            response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
            jsondata = response.json()
            res.append(jsondata)
        return JsonResponse(res, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class PromoDetail(APIView):
    def get_object(self, pk):
        try:
            return ProduitEnPromotion.objects.get(pk=pk)
        except ProduitEnPromotion.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        prod = self.get_object(pk)

        serializer = ProduitEnPromotionSerializer(prod)
        response = requests.get(baseUrl+'product/'+str(serializer.data['tigID'])+'/')
        jsondata = response.json()
        return Response(jsondata)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"


class ShipList(APIView):
    def get(self, request, format=None):
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        return JsonResponse(jsondata, safe=False)
#    def post(self, request, format=None):
#        NO DEFITION of post --> server will return "405 NOT ALLOWED"

class ShipDetails(APIView):
    def get_object(self, pk):
        try:
            return ShipPoints.objects.get(pk=pk)
        except ShipPoints.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        res=[]
        response = requests.get(baseUrl+'shipPoints/')
        jsondata = response.json()
        
        for i in jsondata:
            if i['id']==pk:
                res.append(i)
            
        return JsonResponse(res, safe=False)
#    def put(self, request, pk, format=None):
#        NO DEFITION of put --> server will return "405 NOT ALLOWED"
#    def delete(self, request, pk, format=None):
#        NO DEFITION of delete --> server will return "405 NOT ALLOWED"