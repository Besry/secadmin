# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    blog_user = models.ForeignKey(User)
    content = models.TextField(null=False)
    direction = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    time = models.CharField(max_length=30)
    week = models.IntegerField()

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.content


class CTF_learning(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    type = models.CharField(max_length=20)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title


class ON_DUTY(models.Model):
    time = models.CharField(max_length=30)
    name = models.CharField(max_length=100)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.time


class Book(models.Model):
    TYPE_CHOICES = (
        ('web', '网络'),
        ('re', '逆向'),
        ('program', '开发'),
        ('system', '系统'),
        ('other', '其他'),
    )
    name = models.CharField(max_length=30)
    storage_time = models.DateTimeField(auto_now_add=True)
    lend_time = models.DateTimeField(null=True, blank=True)
    lend_people = models.ForeignKey(User, null=True, blank=True)
    is_lend = models.BooleanField(default=False)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to='bookimages/%Y/%m', verbose_name='缩略图', null=True, blank=True)

    def __str__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.name
