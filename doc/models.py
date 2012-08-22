# encoding=utf-8

from django.db import models


ORG_CHOICES = (
    ('0', '所有组织'),
    ('1', '团委'),
    ('2', '学生会'),
    ('3', '科协'),
    ('4', '体协'),
    ('5', '紫荆'),
    ('6', '核心'),
    ('7', 'TMS'),
    )

class DocPub(models.Model):
    org=models.CharField('组织',max_length=1,choices=ORG_CHOICES,default='0')
    file_name=models.CharField('文件名',max_length=50)
    file_path=models.CharField('文件路径',max_length=100)
    upload_time=models.DateTimeField('上传日期')

    class Meta:
        verbose_name="文件下发"
        verbose_name_plural="文件下发"

    def __str__(self):
        return self.file_name