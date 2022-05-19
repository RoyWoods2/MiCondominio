# Generated by Django 3.1.7 on 2022-05-18 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220518_0339'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': ''}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Precio de'),
        ),
    ]