# Generated by Django 3.1.6 on 2021-02-15 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(related_name='favorited_by', to='bars.Bar'),
        ),
    ]
