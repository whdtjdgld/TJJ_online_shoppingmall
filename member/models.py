from django.db import models
from member.choice import GENDER_CHOICE, STYLE_CHOICE, JOB_CHOICE, ADDRESS_CHOICE

# Create your models here.
class Sign( models.Model ) :
    user_id = models.CharField(max_length=20, verbose_name="아이디", null=False, unique=True, primary_key=True)
    password = models.CharField(max_length=50, verbose_name="비밀번호")
    email = models.EmailField(max_length=100, verbose_name="이메일", null=False, unique=True)
    tel = models.CharField(max_length=15, verbose_name="핸드폰", null=False, unique=True)
    name = models.CharField(max_length=15, verbose_name="이름", null=False)
    birth = models.DateField(auto_now_add=False, verbose_name="생년월일", null=False, blank=False)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=5, verbose_name="성별", null=False)
    address = models.CharField(choices=ADDRESS_CHOICE, max_length=10, verbose_name="시", null=False)
    style = models.CharField(choices=STYLE_CHOICE, max_length=20, verbose_name="옷 스타일", null=False)
    job = models.CharField(choices=JOB_CHOICE, max_length=30, verbose_name="직업", default=6 )