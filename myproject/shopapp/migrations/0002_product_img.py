# Generated by Django 4.2.4 on 2023-09-10 09:05

from django.db import migrations, models
import shopapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=shopapp.models.product_img_path),
        ),
    ]
