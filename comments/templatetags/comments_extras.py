__author__ = 'Luguaa'
__date__ = '2020/5/8 16:14'

from django import template
from ..forms import CommentForm

register = template.Library()


@register.inclusion_tag('inclusions/_form.html', takes_context=True)
def show_comment_form(context, post, form=None):
    """
    评论框
    :param context:
    :param post:
    :param form:
    :return:
    """
    if form is None:
        form = CommentForm()
    return {
        'form': form,
        'post': post,
    }


@register.inclusion_tag('inclusions/_list.html', takes_context=True)
def show_comments(context, post):
    """
    评论展示框
    :param context:
    :param post:
    :return:
    """
    comment_list = post.comments_set.all().order_by('-created_time')
    comment_count = comment_list.count()
    return {
        'comment_count': comment_count,
        'comment_list': comment_list,
    }

