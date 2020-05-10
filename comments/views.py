from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages

from article.models import Post
from .forms import CommentForm
from .models import Comments


# Create your views here.
class CommentView(View):
    """
    评论视图
    """
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(request, messages.SUCCESS, '评论发表成功！', extra_tags='success')
            return redirect(post)

        context = {
            'post': post,
            'form': form,
        }
        messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
        return render(request, 'preview.html', context=context)


