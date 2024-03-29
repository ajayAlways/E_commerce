# Generated by Django 3.1 on 2020-11-05 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=264, null=True)),
                ('category', models.CharField(blank=True, choices=[('MenFashion', 'MenFashion'), ('WomenFashion', 'WomenFashion'), ('KidsFashion', 'KidsFashion'), ('Watches', 'Watches'), ('Shoes', 'Shoes')], max_length=264)),
                ('price', models.FloatField()),
                ('image', models.URLField()),
                ('description', models.TextField(max_length=500)),
                ('digital', models.BooleanField(default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=264, null=True)),
                ('city', models.CharField(max_length=264, null=True)),
                ('pincode', models.CharField(max_length=264, null=True)),
                ('state', models.CharField(max_length=264, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.customer')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_orderd', models.DateTimeField(auto_now_add=True, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base_app.customer')),
            ],
        ),
    ]
