from django.urls import path
from . import views
from .htmx_views import CheckProductHTMX, SaveProductHTMX, DeleteProductHTMX


urlpatterns = [
    path('list_products/', views.list_products, name='list_products'),
]

htmx_urlpatterns = [
    path('check_product/', CheckProductHTMX.as_view(), name='check_product'),
    path('save_product/', SaveProductHTMX.as_view(), name='save_product'),
    path('delete_product/<int:id>/', DeleteProductHTMX.as_view(), name='delete_product'),
]

urlpatterns += htmx_urlpatterns
