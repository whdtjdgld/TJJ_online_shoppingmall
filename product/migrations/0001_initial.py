# Generated by Django 3.2.3 on 2021-06-03 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pnum', models.AutoField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='상품코드')),
                ('pname', models.CharField(max_length=100, unique=True, verbose_name='상품명')),
                ('price', models.IntegerField(unique=True, verbose_name='가격')),
                ('pdate', models.DateField(verbose_name='상품 등록일')),
                ('psum', models.CharField(max_length=300, verbose_name='상품 설명')),
                ('bcate', models.CharField(choices=[('Ring', 'Ring'), ('Necklace', 'Necklace'), ('Earring', 'Earring'), ('Bracelet', 'Bracelet')], max_length=20, verbose_name='대분류')),
                ('mcate', models.CharField(choices=[('Bangle', 'Bangle'), ('Diamond', 'Diamond'), ('Pearl & Gem', 'Pearl & Gem'), ('String & Leather', 'String & Leather'), ('Long', 'Long'), ('Luxury', 'Luxury'), ('Pendant', 'Pendant'), ('Round', 'Round'), ('Y-drop', 'Y-drop'), ('Basic & Bubble', 'Basic & Bubble'), ('묵주', '묵주'), ('Basic Pin', 'Basic Pin')], max_length=20, verbose_name='중분류')),
                ('best', models.CharField(choices=[('등록', '등록'), ('미등록', '미등록')], max_length=20, null=True, verbose_name='베스트셀러 선택')),
                ('image', models.ImageField(blank=True, null=True, upload_to='static/img/', verbose_name='상품 이미지')),
            ],
        ),
    ]
