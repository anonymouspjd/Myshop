# Generated by Django 4.0.2 on 2022-03-23 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_product_seller_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('products', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('shipping', models.IntegerField(default=0)),
                ('finalAmount', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'No Packed'), (2, 'Packed'), (3, 'Out for Delivery'), (4, 'Delivered')], default=1)),
                ('paymentStatus', models.IntegerField(choices=[(1, 'Pending'), (2, 'Success')], default=1)),
                ('mode', models.IntegerField(choices=[(1, 'COD'), (2, 'Net Banking')], default=1)),
                ('time', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('orderId', models.CharField(blank=True, default=None, max_length=50)),
                ('paymentId', models.CharField(blank=True, default=None, max_length=50)),
                ('paymentsignature', models.CharField(blank=True, default=None, max_length=50)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer')),
            ],
        ),
    ]
