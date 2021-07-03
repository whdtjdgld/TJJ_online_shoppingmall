# Generated by Django 3.2.3 on 2021-06-04 07:29

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('product', '0002_alter_product_pnum'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.sign', verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='order',
            name='prod_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='상품코드'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quan',
            field=models.PositiveSmallIntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='수량'),
        ),
    ]
