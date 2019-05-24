from django.contrib import admin
from .models import Product, Author, Publishing_House, Consignee

admin.site.register(Product)
admin.site.register(Author)
admin.site.register(Publishing_House)
admin.site.register(Consignee)
# Register your models here.
