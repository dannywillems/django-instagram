# Generated by Django 2.1 on 2018-09-05 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0004_auto_20180815_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='picture',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]