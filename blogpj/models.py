from django.db import models

# Create your models here.

from django.db import  models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """
    分类模型
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 内部类通过指定一些属性来规定这个类该有的一些特性
    class Meta:
        ordering = ['-create_time']

    # 文章标题及正文
    title = models.CharField(max_length=70)
    body = models.TextField()
    # 文章创建时间及最后一次修改时间
    create_time = models.DateTimeField()
    last_modified_time = models.DateTimeField()
    # 文章摘要，参数设置为允许空置
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章分类、标签、作者，数据表关系连接
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # 部分工具函数,获取相应视图函数的url并解析返回
    def get_absolute_url(self):
        return reverse('blogpj:detail', kwargs={'pk': self.pk})
