from django.urls import path
from shopapp import views


urlpatterns = [
    path('client_products/', views.ClientProductsView.as_view()),
    path('product/', views.ProductView.as_view()),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'), 
]

