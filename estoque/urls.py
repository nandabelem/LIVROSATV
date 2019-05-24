from django.urls import path
from .views import list_products, create_product, update_product, delete_product, json_products

#
urlpatterns = [

	### URLS CRUD - CREATE, READ, UPDATE, DELETE ###

	#READ
	path('',list_products, name='list_products'),
	
	#CREATE
	#path('new', create_product, name='create_product'),
	
	#UPDATE
	#path('update/<int:id>/', update_product, name='update_product'),
	
	#DELETE
	#path('delete/<int:id>/', delete_product, name='delete_product'),


	### GET JSON

	path('json_products', json_products, name='json_products'),

]