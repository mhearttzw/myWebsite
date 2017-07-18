
from django import template
from django.db.models.aggregates import Count
from ..models import Post, Tag, Category


register = template.Library()


# 最新文章标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]


# 按月归档文章标签
@register.simple_tag
def archives():
    return Post.objects.dates('create_time', 'month', order='DESC')


# 分类文章标签
@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    category_list = Category.objects.annotate(num_posts=Count('post'))
    return category_list


# 