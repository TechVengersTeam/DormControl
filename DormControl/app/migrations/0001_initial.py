# Generated by Django 4.2.1 on 2023-05-21 03:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GatePass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('libid', models.CharField(max_length=30)),
                ('stype', models.CharField(max_length=30)),
                ('reason', models.CharField(max_length=30)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('intime', models.TimeField()),
                ('outtime', models.TimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
