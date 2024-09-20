from django.views import View
from django.views.generic import CreateView
from django.shortcuts import render, get_object_or_404
from .models import Product 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CheckProductHTMX(View):
    def get(self, request):
        product = request.GET.get('product', '') 
        if len(product) >= 2:
            search_product = Product.objects.filter(name__iexact=product)
            if search_product.exists():
                return render(request, 'partials/htmx_components/check_product.html', {'product_exists': True})
            else:
                return render(request, 'partials/htmx_components/check_product.html', {'product_exists': False})
        return HttpResponse()  
    
class SaveProductHTMX(View):
    
    def post(self, request):
        name = request.POST.get('product')
        price = request.POST.get('price')
        Product.objects.create(
            name=name,
            price=price
        )
        products = Product.objects.all()
        return render(request, 'partials/htmx_components/list_products.html', {'products': products})
    
@method_decorator(csrf_exempt, name='dispatch')
class DeleteProductHTMX(View):
    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        products = Product.objects.all()
        return render(request, 'partials/htmx_components/list_products.html', {'products': products})