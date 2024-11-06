from itertools import product
from tkinter.font import names

from django.urls import path, include
from rest_framework_nested.routers import NestedDefaultRouter

from . import views
from rest_framework.routers import SimpleRouter, DefaultRouter

# route = SimpleRouter()
# route = DefaultRouter()

route = DefaultRouter()

route.register("collections", views.CollectionViewSet, basename="collections")
route.register("products", views.ProductViewSet, basename="products")
route.register("shoppingcart", views.ShoppingCartViewSet, basename="shoppingcart")

product_route = NestedDefaultRouter(route, "products", lookup="product")
product_route.register("reviews", views.ReviewViewSet, basename="reviews")


# urlpatterns = route.urls

urlpatterns = route.urls + product_route.urls

# urlpatterns = [
#     # path('products/', views.ProductListAPIView.as_view()),
#     #
#     # path('products/<pk>', views.ProductDetailAPIView.as_view()),
#     #
#     # path('collections/', views.CollectionListAPIView.as_view()),
#     #
#     # # the name added was because of the hyperlink in productserilizer class in serializers.py store
#     # path('collections/<pk>', views.CollectionDetailAPIView.as_view(), name='collection-detail',),
#     path('',include(route.urls)),
#     path('',include(product_route.urls)),
# ]