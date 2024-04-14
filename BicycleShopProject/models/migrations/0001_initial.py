# Generated by Django 4.0.6 on 2024-04-14 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('brand_id', models.IntegerField(primary_key=True, serialize=False)),
                ('brand_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'brands',
            },
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('order_status', models.IntegerField(choices=[(1, 'Pending'), (2, 'Processing'), (3, 'Rejected'), (4, 'Completed'), (5, 'Draft')])),
                ('order_date', models.DateField()),
                ('required_date', models.DateField()),
                ('shipped_date', models.DateField(blank=True, null=True)),
                ('customer_id', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='models.customer')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255)),
                ('model_year', models.SmallIntegerField()),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('brand_id', models.ForeignKey(db_column='brand_id', on_delete=django.db.models.deletion.CASCADE, to='models.brand')),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.CASCADE, to='models.categorie')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.IntegerField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=25, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('street', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=25, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'stores',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(db_column='staff_id', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('manager_id', models.ForeignKey(blank=True, db_column='manager_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='models.staff')),
                ('store_id', models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='models.store')),
            ],
            options={
                'db_table': 'staffs',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('order_id', models.ForeignKey(db_column='order_id', on_delete=django.db.models.deletion.CASCADE, to='models.order')),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='models.product')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='staff_id',
            field=models.ForeignKey(db_column='staff_id', on_delete=django.db.models.deletion.CASCADE, to='models.staff'),
        ),
        migrations.AddField(
            model_name='order',
            name='store_id',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='models.store'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('product_id', models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='models.product')),
                ('store_id', models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.CASCADE, to='models.store')),
            ],
            options={
                'db_table': 'stocks',
                'unique_together': {('store_id', 'product_id')},
            },
        ),
    ]