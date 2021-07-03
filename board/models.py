from django.db import models

class Board(models.Model) :
    num = models.IntegerField(verbose_name="글번호", null=False, unique=True)
    writer = models.CharField(max_length=30, verbose_name="작성자", null=False)
    subject = models.CharField(max_length=300, verbose_name="제목", null=False)
    passwd = models.CharField(max_length=20, verbose_name="비밀번호", null=True)
    content = models.CharField(max_length=2000, verbose_name="내용", null=False)
    readcount = models.IntegerField(verbose_name="조회수", default=0)
    ref = models.IntegerField(verbose_name="그룹화 아이디")
    restep = models.IntegerField(verbose_name="글 순서")
    relevel = models.IntegerField(verbose_name="글레벨")
    regdate = models.DateTimeField(auto_now_add=True, verbose_name="작성일", blank=True)
    ip = models.CharField(max_length=30, verbose_name="IP")