# Generated by Django 3.2.3 on 2021-06-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhichMrtName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MrtCode', models.CharField(help_text='Enter Mrt Station Code, ex: R12 = 雙連捷運站', max_length=200)),
                ('MrtName', models.CharField(help_text='Enter Mrt Station Name, ex: R12 = 雙連捷運站', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='buydb',
            name='BuydbMrtName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.whichmrtname'),
        ),
    ]
