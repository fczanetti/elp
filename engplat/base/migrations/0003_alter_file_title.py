# Generated by Django 5.1.6 on 2025-02-09 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(max_length=72, unique=True),
        ),
    ]
