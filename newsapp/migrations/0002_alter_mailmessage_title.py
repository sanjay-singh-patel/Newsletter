# Generated by Django 3.2.7 on 2021-10-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailmessage',
            name='title',
            field=models.TextField(max_length=100),
        ),
    ]
