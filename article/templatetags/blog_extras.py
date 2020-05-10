__author__ = 'Luguaa'
__date__ = '2020/5/7 16:22'

from django import template

from ..models import Post, Category, Tag

register = template.Library()


@register.inclusion_tag('inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    """
    侧边栏最新文章
    """
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('inclusions/_archives.html', takes_context=True)
def show_archives(context):
    """
    侧边栏按月归档
    """
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('inclusions/_categories.html', takes_context=True)
def show_categories(context):
    """
    侧边栏按分类归档
    """
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('inclusions/_tags.html', takes_context=True)
def show_tags(context):
    """
    侧边栏标签
    """
    return {
        'tag_list': Tag.objects.all(),
    }

