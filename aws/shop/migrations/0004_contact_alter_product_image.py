# Generated by Django 4.1 on 2022-09-12 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=3030)),
                ('email', models.CharField(default='', max_length=5030)),
                ('phone', models.CharField(default='', max_length=5030)),
                ('query', models.CharField(default='', max_length=30030)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
