# Generated by Django 3.2.3 on 2021-06-15 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_recommend_u_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommend',
            name='member',
            field=models.CharField(max_length=100, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='recommend',
            name='product',
            field=models.IntegerField(verbose_name='추천상품번호'),
        ),
    ]
