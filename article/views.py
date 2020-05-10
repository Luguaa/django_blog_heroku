import markdown
from markdown.extensions.toc import TocExtension

from django.shortcuts import render
from django.views.generic.base import View
from django.utils.text import slugify

from .models import Post, Category, Tag


# Create your views here.
class IndexView(View):
    """
    首页视图
    """
    def get(self, request):
        post_list = Post.objects.all().order_by('-created_time')
        return render(request, 'index.html', context={
            'post_list': post_list
        })


class DetailView(View):
    """
    文章详情页
    """
    def get(self, request, id):
        post = Post.objects.get(id=id)
        md = markdown.Markdown(extensions=[
                                  'markdown.extensions.extra',
                                  'markdown.extensions.fenced_code',
                                  TocExtension(slugify=slugify),
                              ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return render(request, 'detail.html', context={
            'post': post
        })


class DateView(View):
    """
    侧边栏日期归档
    """

    def get(self, request, year, month):

        post_list = Post.objects.filter(created_time__year=year,
                                        created_time__month=month
                                        ).order_by('-created_time')

        return render(request, 'index.html', context={
            'post_list': post_list
        })


class CategoryView(View):
    """
    侧边栏分类
    """
    def get(self, request, id):
        # 记得在开始部分导入 Category 类
        category = Category.objects.get(id=id)

        post_list = Post.objects.filter(category=category).order_by('-created_time')

        return render(request, 'index.html', context={
            'post_list': post_list
        })


class TagView(View):
    """
    侧边栏标签
    """
    def get(self, request, id):
        # 记得在开始部分导入 Category 类
        tag = Tag.objects.get(id=id)

        post_list = Post.objects.filter(tags=tag).order_by('-created_time')

        return render(request, 'index.html', context={
            'post_list': post_list
        })


