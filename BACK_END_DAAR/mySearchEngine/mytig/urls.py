from django.urls import path
from mytig import views

urlpatterns = [
    path('products/', views.RedirectionListeDeProduits.as_view()),
    path('product/<int:pk>/', views.RedirectionDetailProduit.as_view()),
    path('shipPoints/', views.ShipList.as_view()),
    path('shipPoint/<int:pk>/', views.ShipDetails.as_view()),
    
    path('availableproducts/', views.AvailableProducts.as_view()),
    path('availableproduct/<int:pk>/', views.AvailableProductDetail.as_view()),
    
    
    path('onsaleproducts/', views.PromoList.as_view()),
    path('onsaleproduct/<int:pk>/', views.PromoDetail.as_view()),

    
    


]
