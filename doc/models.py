# encoding=utf-8

from django.db import models
from datetime import datetime
from django.contrib.auth.models import Group

NOW=datetime.now()
UPLOAD_PATH="./upload/"+str(NOW.year)+"/"+str(NOW.month)+"/"+str(NOW.day)

class DocPub(models.Model):
    org=models.ForeignKey(Group,verbose_name='组织')
    file_name=models.FileField('文件名',max_length=50,upload_to=UPLOAD_PATH)
    file_description=models.TextField('文件描述',max_length=1000)
    upload_time=models.DateTimeField('上传日期')

    class Meta:
        verbose_name="文件下发"
        verbose_name_plural="文件下发"

    def __unicode__(self):
        return self.file_name