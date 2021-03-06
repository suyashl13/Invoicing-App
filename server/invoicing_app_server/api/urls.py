from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),
    path('auth/', include('api.kauth.urls')),
    path('user/', include('api.users.urls')),
    path('shop/', include('api.shop.urls')),
    path('purchase-order/', include('api.purchase_orders.urls'))
]
