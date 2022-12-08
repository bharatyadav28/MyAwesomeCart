# Generated by Django 4.1 on 2022-09-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_contact_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('json_items', models.CharField(default='', max_length=303)),
                ('name', models.CharField(default='', max_length=303)),
                ('email', models.CharField(default='', max_length=503)),
                ('phone', models.CharField(default='', max_length=503)),
                ('address1', models.CharField(default='', max_length=300)),
                ('address2', models.CharField(default='', max_length=300)),
                ('city', models.CharField(default='', max_length=300)),
                ('state', models.CharField(default='', max_length=300)),
                ('zip', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
