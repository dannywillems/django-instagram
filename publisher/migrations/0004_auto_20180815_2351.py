# Generated by Django 2.1 on 2018-08-15 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0003_auto_20180815_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='instagram_account_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='publisher.InstagramAccount'),
            preserve_default=False,
        ),
    ]
