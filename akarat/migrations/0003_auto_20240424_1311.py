# Generated by Django 3.2.12 on 2024-04-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akarat', '0002_auto_20240420_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type_compte',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
