from django.shortcuts import render
from django.views import View
from .models import Post

# Create your views here.


# ## 게시글
class Index(View):
    def get(self, request):
        posts = Post.objects.all()
        context = {
            'title': 'Blog',
            'posts': posts,
        }
        return render(request, 'blog/post_list.html', context)


class DetailView(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            'title': 'Blog',
            'post': post,
        }
        return render(request, 'blog/post_detail.html', context)
