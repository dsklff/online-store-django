# Generated by Django 3.0.8 on 2020-08-02 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200802_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='placeholder.png', null=True, upload_to=''),
        ),
    ]
