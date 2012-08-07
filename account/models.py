# encoding=utf-8

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
    )

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, verbose_name='用户')
    mobile = models.CharField('手机', max_length=11, blank=True, null=True)
    address = models.CharField('宿舍', max_length=100, blank=True, null=True)
    website = models.URLField('个人主页', blank=True, null=True)
    birthday = models.DateField('生日', blank=True, null=True)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='M')
    QQ = models.CharField('QQ', max_length=11, blank=True, null=True)

    class Meta:
        verbose_name="用户资料"
        verbose_name_plural="用户资料"

