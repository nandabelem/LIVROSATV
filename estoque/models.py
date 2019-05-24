from django.db import models


class Author(models.Model):
	author_id = models.AutoField(primary_key=True)
	author_name = models.CharField(max_length=20)

	def __str__(self):
		return self.author_name

class Publishing_House(models.Model):
	publishing_house_id = models.AutoField(primary_key=True)
	publishing_house_name = models.CharField(max_length=20)

	def __str__a(self):
		return self.publishing_house_name

class Consignee(models.Model):
	consignee_id = models.AutoField(primary_key=True)
	consignee_name = models.CharField(max_length=100)
	consignee_email = models.EmailField()

	def __str__(self):
		return self.consignee_name

class Product(models.Model):
	product_id = models.AutoField(primary_key=True)
	product_description = models.CharField(max_length=300)
	product_quantity = models.IntegerField()
	product_buy_price = models.DecimalField(max_digits=9, decimal_places=2)
	product_sale_price = models.DecimalField(max_digits=9, decimal_places=2)
	product_photo = models.URLField()
	product_status = models.CharField(
	    max_length=20,
	    choices=(
	        ('available', 'DISPONÍVEL'),
	        ('in_stock', 'EM ESTOQUE'),
	        ('reserved','RESERVADO'),
	        ('sold', 'VENDIDO'),
    	)
	)
	product_type = models.CharField(
	    max_length=20,
	    choices=(
	        ('book', 'LIVRO'),
		    ('frame', 'QUADRO'),
	   	)
	)

	### FOREIGN KEYS

	product_consignee = models.ForeignKey(
		Consignee, on_delete = models.CASCADE)


	### IF PRODUCT IS BOOK ###

	product_book_name = models.CharField(max_length=100)
	product_book_year = models.CharField(max_length=4)
	product_book_author = models.ForeignKey(
		Author, on_delete = models.CASCADE)	
	product_book_publishing_house = models.ForeignKey(
		Publishing_House, on_delete = models.CASCADE)

	def __str__(self):
		return self.product_description



	

		