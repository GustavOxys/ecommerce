# Generated by Django 5.0.6 on 2024-05-31 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_variation_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('V', 'Variable'), ('S', 'Simple')], default='V', max_length=1),
        ),
    ]
