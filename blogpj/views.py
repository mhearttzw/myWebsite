from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
from comment.forms import CommentForm


import markdown

# Create your views here.


def search(request):
    q = request.GET.get('searchKey')
    error_msg = ''
    if not q:
        error_msg = '请输入关键词'
        return render(request, 'blogpj/index.html', {'error_msg': error_msg})
    # 搜索title中含有关键词的文章，icontains是查询表达式(Field lookups),用法是在模型需要筛选的属性后面加两个下划线
    post_list = Post.objects.filter(title__icontains=q)
    return render(request, 'blogpj/index.html', {'error_msg': error_msg,
                                                   'post_list': post_list})


def index(request):
    post_list = Post.objects.all()
    # post_list = Post.objects.all().order_by('-create_time')
    # 很明显，render函数会自动渲染到template目录下
    return render(request, 'blogpj/index.html', context={
        'post_list': post_list
    })
    #return HttpResponse("这是欢迎首页！")


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                   extensions=[
                                       'markdown.extensions.extra',
                                       # 语法高亮扩展
                                       'markdown.extensions.codehilite',
                                       # 允许自动生成目录
                                       'markdown.extensions.toc'
                                   ])
    form = CommentForm()
    # 获取文章下全部评论
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }
    return render(request, 'blogpj/detail.html', context=context)


# 按日期分类
def archives(request, year, month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month
                                    )
    return render(request, 'blogpj/index.html', context={'post_list': post_list})


# 分类
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blogpj/index.html', context={'post_list': post_list})
