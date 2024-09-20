from django.views import View
from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

class CheckProductHTMX(View):
    def get(self, request):
        product = request.GET.get('product', '') 
        if len(product) >= 3:
            search_product = Product.objects.filter(name__iexact=product)
            if search_product.exists():
                return render(request, 'partials/htmx_components/check_product.html', {'product_exists': True})
            else:
                return render(request, 'partials/htmx_components/check_product.html', {'product_exists': False})
        return HttpResponse()  