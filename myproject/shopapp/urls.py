from django.urls import path
from shopapp import views

urlpatterns = [
    path('client_products/', views.ClientProductsView.as_view()),
]
