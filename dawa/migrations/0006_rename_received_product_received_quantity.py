# Generated by Django 4.1.7 on 2023-04-01 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dawa', '0005_alter_sale_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='received',
            new_name='received_quantity',
        ),
    ]
