# Generated by Django 3.2.7 on 2021-10-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_alter_mailmessage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailmessage',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
