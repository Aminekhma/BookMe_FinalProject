from django.urls import path
from mygutenberg import views

urlpatterns = [
    path('books/', views.listBooks.as_view()),
    path('books/<int:pk>/', views.detailBook.as_view()),
    # path('frenchbooks/', views.RedirectionListeDeProduits.as_view()),
    # path('frenchbooks/<int:pk>/', views.ShipDetails.as_view()),
    # path('englishbooks/', views.RedirectionListeDeProduits.as_view()),
    # path('frenchbooks/<int:pk>/', views.ShipDetails.as_view()),
    path('Search/<str:word>/', views.SearchAPI.as_view()),
    path('RegexSearch/<str:word>/', views.SearchRegexAPI.as_view()),




    
    


]
