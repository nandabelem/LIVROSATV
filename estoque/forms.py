from django import forms
from .models import Product


class ProductForm(forms.Form):

	class Meta:
		
		model = Product

		fields = ('product_description', 'product_photo','product_quantity', 'product_buy_price', 'product_sale_price',
						'product_consignee','product_status', 'product_book_name','product_book_year', 'product_book_author',
						'product_book_publishing_house')
		








	
	


