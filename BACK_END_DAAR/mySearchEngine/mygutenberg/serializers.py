from rest_framework.serializers import ModelSerializer
from mygutenberg.models import listOFBooks,BookIndex,BookGraphJaccard
        
        
class listOFBooksSerializer(ModelSerializer):
    class Meta:
        model = listOFBooks
        fields = ('id', 'title','author','language','imageBook','text','crank')

class BookIndexSerializer(ModelSerializer):
    class Meta:
        model = BookIndex
        fields = ('id','title', 'wordOcc')
        
class BookGraphJaccardSerializer(ModelSerializer):
    class Meta:
        model = BookGraphJaccard
        fields = ('id','neightbors')