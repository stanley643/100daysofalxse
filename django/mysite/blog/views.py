from calendar import day_abbr, month, year
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__year=year,
                            publish__month=month,
                            publish__day=day_abbr)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})