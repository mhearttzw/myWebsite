

from django.shortcuts import render, get_object_or_404, redirect
from blogpj.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.


def post_comment(request, post_pk):
    # 获取post
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中，这是一个类字典对象
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来
            comment.post = post
            # 最终将评论数据保存进数据库，调用模型实例的save方法
            comment.save()
            # 当redirect函数接收一个模型的实例时，它会调用这个模型实例的get_absolute_url方法，
            # 然后重定向到get_absolute_url方法返回的URL
            return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blogpj/detail.html', context=context)
    print("post这里出错了！")
    return redirect(post)
