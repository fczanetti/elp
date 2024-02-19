# Generated by Django 5.0.2 on 2024-02-19 13:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpayment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpayment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='payments.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userpayment',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]