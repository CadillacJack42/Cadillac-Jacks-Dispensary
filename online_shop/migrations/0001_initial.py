# Generated by Django 3.1.5 on 2021-01-22 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('FL', 'Flower'), ('CC', 'Concentrate'), ('CT', 'Cartridge'), ('ED', 'Edible'), ('OT', 'Other')], default='FL', max_length=2)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('IN', 'Indica'), ('SA', 'Sativa'), ('HY', 'Hybrid')], default='HY', max_length=2)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'variety',
                'verbose_name_plural': 'varieties',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('thc', models.DecimalField(decimal_places=3, max_digits=6)),
                ('cbd', models.DecimalField(decimal_places=3, max_digits=6)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='online_shop.category')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='online_shop.variety')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
