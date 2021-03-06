# Generated by Django 3.2.5 on 2021-07-14 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Packed', 'Packed'), ('Arriving', 'Arriving'), ('Accepted', 'Accepted'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('TW', 'Top Wear'), ('M', 'Mobile'), ('L', 'Laptop'), ('BW', 'Bottom Wear')], max_length=2),
        ),
    ]
