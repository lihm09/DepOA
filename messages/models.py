# encoding=utf-8

from django.db import models

class Situation(models.Model):
    '''
    用来给留言分类
    '''
    name = models.CharField(max_length=30)
    time = models.DateField()

    def __unicode__(self):
        return self.name

class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20)
    situation = models.ForeignKey(Situation)

    class Meta:
        ordering = ['-time']

    def __unicode__(self):
        return self.name





