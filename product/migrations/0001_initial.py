# Generated by Django 5.0.6 on 2024-05-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_short', models.TextField(max_length=255)),
                ('description_long', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/%Y/%m/')),
                ('slug', models.SlugField(unique=True)),
                ('price_marketing', models.FloatField()),
                ('price_marketing_promotional', models.FloatField(default=0)),
                ('type', models.CharField(choices=[('V', 'Variation'), ('S', 'Simple')], default='V', max_length=1)),
            ],
        ),
    ]
