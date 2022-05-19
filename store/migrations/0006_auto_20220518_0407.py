# Generated by Django 3.1.7 on 2022-05-18 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20220518_0345'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={'verbose_name': 'Imagen Referencial', 'verbose_name_plural': 'Imagen Referencial'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.category', verbose_name='Abreviacion'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': ''}}, help_text='Maximo $999.99', max_digits=5, verbose_name='Descuento Disponible'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, help_text='', verbose_name='¿Area Privada?'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='store.producttype', verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': ''}}, help_text='Maximo de $999', max_digits=5, verbose_name='Precio'),
        ),
    ]
