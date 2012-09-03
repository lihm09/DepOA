# encoding=utf-8

from django.db import models
from django.contrib.auth.models import User

GENDER_CHOICES = (
    ('M', '男'),
    ('F', '女'),
)

GRADE_CHOICES = (
    ('0','零字班'),
    ('1','一字班'),
    ('2','二字班'),
    ('3','三字班'),
    ('4','四字班'),
    ('5','五字班'),
    ('6','六字班'),
    ('7','七字班'),
    ('8','八字班'),
    ('9','九字班'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, verbose_name='用户')
    student_number = models.CharField('学号',unique=True, max_length=10)
    grade = models.CharField('年级' ,max_length=1, choices=GRADE_CHOICES, default='0')
    class_name = models.CharField('班级', max_length=5)
    mobile = models.CharField('手机',unique=True, max_length=11)
    address = models.CharField('宿舍', max_length=15, blank=True, null=True)
    gender = models.CharField('性别', max_length=1, choices=GENDER_CHOICES, default='M')
    website = models.URLField('个人主页', blank=True, null=True)
    birthday = models.DateField('生日', blank=True, null=True)

    class Meta:
        verbose_name="用户资料"
        verbose_name_plural="用户资料"

    def __unicode__(self):
        return self.user.username