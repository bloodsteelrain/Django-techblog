from django.shortcuts import render, redirect
from django.views import View
from .models import Post, Category
from .forms import PostForm

# Create your views here.


# ## 게시글
class Index(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        context = {
            'title': 'Blog',
            'posts': posts,
            'categories': Category.objects.all(),
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


class Write(View):
    def get(self, request):
        form = PostForm()
        context = {
            'title': 'Blog',
            'form': form,
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:list')
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            'form': form,
        }
        return render(request, 'blog/post_form.html', context)


class Update(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(initial={'title': post.title, 'content': post.content})
        context = {
            'title': 'Blog',
            'post': post,
            'form': form,
        }
        return render(request, 'blog/post_edit.html', context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect('blog:detail', pk=pk)
        form.add_error(None, '폼이 유효하지 않습니다.')
        context = {
            'title': 'Blog',
            'form': form,
        }
        return render(request, 'blog/post_edit.html', context)


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect('blog:list')


class CategoryView(View):
    def get(self, request, c_name):
        category = Category.objects.get(name=c_name)
        posts = Post.objects.filter(category=category).order_by('-created_at')
        context = {
            'title': 'Blog',
            'posts': posts,
            'categories': Category.objects.all(),
        }
        return render(request, 'blog/post_list.html', context)
