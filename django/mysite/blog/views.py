from calendar import month
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.
def post_list(request):
    posts = Post.published.all()

    #paginator = Paginator(post_list, 3)
    #page_number = request.GET.get('page', 1)
    #posts = paginator.page(page_number)
    

    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post,
                            status=Post.Status.PUBLISHED,
                            slug=post,
                            publish__month=month,
                            publish__day=day)
    
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})

class PostListView(ListView):
    """Alternative post list view"""

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'