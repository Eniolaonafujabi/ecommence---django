from tkinter.font import names

from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),

    path('products/<pk>', views.ProductDetailAPIView.as_view()),

    path('collections/', views.collection_list),

    # the name added was because of the hyperlink in productserilizer class in serializers.py store
    path('collections/<pk>', views.collection_details, name='collection-detail',),
]