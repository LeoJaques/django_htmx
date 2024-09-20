from django.urls import path
from . import views
from .htmx_views import CheckProductHTMX


urlpatterns = [
    path('list_products/', views.list_products, name='list_products'),
]

htmx_urlpatterns = [
    path('check_product/', CheckProductHTMX.as_view(), name='check_product' )
]

urlpatterns += htmx_urlpatterns