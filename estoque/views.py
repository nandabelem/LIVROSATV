from django.shortcuts import render
from .forms import ProductForm
from .models import Product
from django.http import JsonResponse

### Acessa lista no banco e devolve para o navegador

### READ ###

def list_authors(request):
	author = Author.objects.all()
	return render(request, 'author.html',{'author': author})

def list_publishing_houses(request):
	publishing_house = Publishing_House.objects.all()
	return render(request, 'publishing_house.html',{'publishing_house': publishing_house})

def list_consignees(request):
	consignee = Consignee.objects.all()
	return render(request, 'consignee.html',{'consignee': consignee})

def list_products(request):
	products = Product.objects.all()
	return render(request, 'products.html',{'products': products})


### CREATE ###


def create_product(request):

	form = ProductForm(request.POST or None)
 
	if form.is_valid():

	    form.save()
	    return redirect('list_products')
        
	return render(request, 'products_form.html', {'form': form})


def update_product(request, id):

    product = Product.objects.get(id=id)

    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():

        form.save()
        return redirect('list_products')

    return render(request, 'products-form.html', {'form': form, 'product': product})


def delete_product(request, id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':

        product.delete()
        return redirect('list_products')

    return render(request, 'prod-delete-confirm.html', {'product': product})

def json_products(request):
	
    products = Product.objects.all().values()  # or simply .values() to get all fields
    products_list = list(products)  # important: convert the QuerySet to a list object

    return JsonResponse(products_list, safe=False)
