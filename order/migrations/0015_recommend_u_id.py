# Generated by Django 3.2.3 on 2021-06-15 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20210614_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommend',
            name='u_id',
            field=models.IntegerField(default=2, verbose_name='회원번호'),
            preserve_default=False,
        ),
    ]
