from rest_framework.serializers import ModelSerializer
from mytig.models import ProduitEnPromotion
from mytig.models import ShipPoints

class ProduitEnPromotionSerializer(ModelSerializer):
    class Meta:
        model = ProduitEnPromotion
        fields = ('id', 'tigID')
        
class ShipPointSerializer(ModelSerializer):
    class Meta:
        model = ShipPoints
        fields = ('id', 'tigID')
