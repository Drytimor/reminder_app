# Generated by Django 5.0.2 on 2024-02-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_events_number_clients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Название'),
        ),
    ]