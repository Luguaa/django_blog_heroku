from datetime import datetime

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    """
    分类 Category
    """
    name = models.CharField(max_length=10, verbose_name="分类名称")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签 Tag
    """
    name = models.CharField(max_length=10, verbose_name="标签名")

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
    title = models.CharField(max_length=70, verbose_name="标题")
    body = models.TextField(verbose_name="文章")
    created_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=datetime.now)
    modified_time = models.DateTimeField(verbose_name="最后一次修改时间", auto_now=datetime.now)
    excerpt = models.CharField(max_length=200, blank=True, null=True, verbose_name="摘要")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="标签")

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article:detail', args=[str(self.id)])

