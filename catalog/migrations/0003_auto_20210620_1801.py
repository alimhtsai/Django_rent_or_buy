# Generated by Django 3.2.3 on 2021-06-20 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210620_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buydb',
            name='BuydbMrtName',
        ),
        migrations.AddField(
            model_name='whichmrtname',
            name='Object',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.buydb'),
        ),
    ]
