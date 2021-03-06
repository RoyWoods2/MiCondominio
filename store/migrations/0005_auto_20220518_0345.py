# Generated by Django 3.1.7 on 2022-05-18 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20220518_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.category', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.producttype', verbose_name='Area'),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': ''}}, help_text='Maximum 999.99', max_digits=5, verbose_name='Regular price'),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='name',
            field=models.CharField(help_text='Required', max_length=255, verbose_name='Nombre'),
        ),
    ]
