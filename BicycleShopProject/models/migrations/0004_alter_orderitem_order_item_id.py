# Generated by Django 4.0.6 on 2024-04-14 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0003_alter_order_required_date_alter_order_staff_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order_item_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
