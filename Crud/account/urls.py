
from django.urls import path,include
from account.views import *

urlpatterns = [
    path('addproduct',AddProductView.as_view(),name="addproduct"),
    path('viewproduct',ViewProductView.as_view(),name="viewproduct"),
    path('viewproduct/<str:category>',FilterView.as_view(),name="filterview"),
    path('deleteproduct/<int:pid>',DeleteProductView.as_view(),name='deleteproduct'),
    path('editproduct/<int:eid>',UpdateProductView.as_view(),name='editproduct')
]