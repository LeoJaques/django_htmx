from django.shortcuts import render

# Create your views here.
def list_products(request):
    return render(request, template_name='list_products.html')