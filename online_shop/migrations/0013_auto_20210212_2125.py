# Generated by Django 3.1.6 on 2021-02-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0012_auto_20210212_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../media/no_image.png', upload_to='products/%Y/%m/%d'),
        ),
    ]
