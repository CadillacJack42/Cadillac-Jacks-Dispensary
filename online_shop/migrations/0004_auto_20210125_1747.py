# Generated by Django 3.1.5 on 2021-01-26 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0003_auto_20210125_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Flower', 'Flower'), ('Concentrate', 'Concentrate'), ('Cartridge', 'Cartridge'), ('Edible', 'Edible'), ('Other', 'Other'), ('Preroll', 'Preroll')], default='Flower', max_length=11),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='name',
            field=models.CharField(choices=[('Ounce', 'Ounce'), ('Quarter', 'Quarter'), ('Eighth', 'Eighth'), ('Gram', 'Gram'), ('Cartridge', 'Cartridge'), ('Package', 'Package'), ('Preroll', 'Preroll')], default='Gram', max_length=9),
        ),
    ]
