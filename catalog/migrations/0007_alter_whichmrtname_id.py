# Generated by Django 3.2.3 on 2021-06-26 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_whichmrtname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whichmrtname',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]