# Generated by Django 3.1.6 on 2021-02-17 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bars', '0001_initial'),
        ('profiles', '0002_profile_favorites'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('bar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bars.bar')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='reference_booking',
            field=models.ManyToManyField(through='profiles.Booking', to='bars.Bar'),
        ),
    ]
