# Generated by Django 3.2.3 on 2021-05-26 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0011_remove_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]