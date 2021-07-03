from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from product.models import Product
from member.models import Sign

# Create your models here.
class Order( models.Model) :
    onum = models.AutoField(verbose_name="주문번호", null=False, unique=True, primary_key=True)
    prod_num = models.ForeignKey(Product, verbose_name="상품코드", on_delete=models.CASCADE)
    order_id = models.ForeignKey(Sign, verbose_name="이름", on_delete=models.CASCADE)
    quan = models.PositiveSmallIntegerField(null=True, default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name="수량")

class Buy(models.Model) :
    bnum = models.AutoField(verbose_name="구매번호", null=False, unique=True, primary_key=True)
    pnum = models.IntegerField(verbose_name="상품코드", null=True)
    pname = models.CharField(max_length=100, verbose_name="상품명", null=True)
    price = models.IntegerField(verbose_name="가격", null=True)
    quan = models.IntegerField(verbose_name="개수", null=True)
    member = models.CharField(max_length=100, verbose_name="이름", null=True)
    pay = models.DateField(auto_now_add=True, verbose_name="주문날짜")
    
class Recommend(models.Model):
    u_id = models.IntegerField(verbose_name="회원번호")
    member =models.CharField(max_length=100, verbose_name="아이디")
    product = models.ForeignKey(Product, verbose_name="추천상품번호", on_delete=models.CASCADE)