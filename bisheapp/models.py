from django.db import models

# Create your models here.
class user(models.Model):
    user=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
class rootuser(models.Model):
    user=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
class Topic(models.Model):
    # t_id = models.CharField(verbose_name='帖子id', max_length=16)
    t_uid = models.CharField(verbose_name='帖子所属用户id', max_length=16)
    t_kind = models.CharField(verbose_name='类别', max_length=32)
    create_time = models.CharField(verbose_name='创建时间',max_length=128)
    t_photo = models.CharField(verbose_name='帖子图片', max_length=128, null=True)
    t_content = models.CharField(verbose_name='帖子正文', max_length=3000)
    t_title = models.CharField(verbose_name='帖子标题', max_length=64)
    t_introduce = models.CharField(verbose_name='帖子简介', max_length=256)
    recommend = models.BooleanField(verbose_name='是否推荐', default=0)
class Kind(models.Model):
    # k_id = models.CharField(verbose_name='分类id', max_length=16)
    k_name = models.CharField(verbose_name='分类名称', max_length=16)
class Announcement(models.Model):
    # a_id = models.CharField(verbose_name='公告id', max_length=16)
    a_title = models.CharField(verbose_name='公告标题', max_length=64)
    a_content = models.CharField(verbose_name='公告内容', max_length=3000, null=True)
