# Generated by Django 3.1.5 on 2021-02-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0007_auto_20210201_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='../media/no_image.jpg', upload_to='products/%Y/%m/%d'),
        ),
    ]
