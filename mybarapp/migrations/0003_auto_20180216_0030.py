# Generated by Django 2.0.2 on 2018-02-16 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybarapp', '0002_auto_20180215_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platillo',
            name='image',
            field=models.ImageField(upload_to='platillos'),
        ),
    ]
