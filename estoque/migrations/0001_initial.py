# Generated by Django 2.0.13 on 2019-05-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False)),
                ('author_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('consignee_id', models.AutoField(primary_key=True, serialize=False)),
                ('consignee_name', models.CharField(max_length=100)),
                ('consignee_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_description', models.CharField(max_length=300)),
                ('product_quantity', models.IntegerField(blank=True)),
                ('product_buy_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_sale_price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('product_photo', models.URLField(blank=True)),
                ('product_status', models.CharField(choices=[('available', 'DISPONÍVEL'), ('in_stock', 'EM ESTOQUE'), ('reserved', 'RESERVADO'), ('sold', 'VENDIDO')], max_length=20)),
                ('product_type', models.CharField(choices=[('book', 'LIVRO'), ('frame', 'QUADRO')], max_length=20)),
                ('product_book_name', models.CharField(max_length=100)),
                ('product_book_year', models.CharField(max_length=4)),
                ('product_book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publishing_House',
            fields=[
                ('publishing_house_id', models.AutoField(primary_key=True, serialize=False)),
                ('publishing_house_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_book_publishing_house',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Publishing_House'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_consignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.Consignee'),
        ),
    ]
