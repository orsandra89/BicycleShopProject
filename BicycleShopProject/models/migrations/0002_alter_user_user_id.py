# Generated by Django 4.0.6 on 2024-04-28 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(db_column='user_id', primary_key=True, serialize=False),
        ),
    ]