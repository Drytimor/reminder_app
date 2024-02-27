# Generated by Django 5.0.2 on 2024-02-13 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_clients', models.IntegerField(default=0, verbose_name='количество клиентов')),
            ],
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='name',
        ),
        migrations.RemoveField(
            model_name='reminder',
            name='role',
        ),
        migrations.CreateModel(
            name='Recordings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reminder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to='core.reminder')),
            ],
        ),
    ]
