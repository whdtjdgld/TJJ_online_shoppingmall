from django.db import models
from product.choice import BCATE_CHOICE, MCATE_CHOICE, BEST_CHOICE

# Create your models here.
class Product(models.Model):
    pnum = models.IntegerField(verbose_name="상품코드", null=False, unique=True, primary_key=True)
    pname = models.CharField(max_length=100, verbose_name="상품명", null=False, unique=True)
    price = models.IntegerField(verbose_name="가격", null=False)
    pdate = models.DateField(auto_now_add=False, verbose_name="상품 등록일", null=False, blank=False)
    psum = models.CharField(max_length=300, verbose_name="상품 설명", null=False)
    bcate = models.CharField(choices=BCATE_CHOICE, max_length=20, verbose_name="대분류", null=False)
    mcate = models.CharField(choices=MCATE_CHOICE, max_length=20, verbose_name="중분류", null=False)
    best = models.CharField(choices=BEST_CHOICE, max_length=20, verbose_name="베스트셀러 선택", null=True)
    image = models.ImageField(upload_to='static/img/',verbose_name="상품 이미지", blank=True, null=True)
    