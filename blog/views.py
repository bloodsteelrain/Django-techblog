from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import HttpResponseForbidden, Http404
from .models import Post, Category, Comment, HashTag, Reply
from .forms import PostForm, CommentForm, HashTagForm

# Create your views here.


# ## 게시글
class Index(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        query = request.GET.get('q')
        search_option = request.GET.get('search_option', 'title+content')
        if query:
            if search_option == 'all':
                posts = Post.objects.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query) |
                    Q(writer__username__icontains=query) |
                    Q(hashtag__name__icontains=query)
                )
            elif search_option == 'title+content':
                posts = Post.objects.filter(
                    Q(title__icontains=query) | Q(content__icontains=query))
            elif search_option == 'title':
                posts = Post.objects.filter(title__icontains=query)
            elif search_option == 'content':
                posts = Post.objects.filter(content__icontains=query)
            elif search_option == 'writer':
                posts = Post.objects.filter(writer__username__icontains=query)
            elif search_option == 'tags':
                posts = Post.objects.filter(hashtag__name__icontains=query)
            posts = posts.order_by('-created_at')
        else:
            posts = Post.objects.all().order_by('-created_at')

        context = {
            'title': 'Blog',
            'posts': posts,
            'categories': Category.objects.all(),
            'query': query,
            'search_option': search_option,
        }
        return render(request, 'blog/post_list.html', context)


class DetailView(View):
    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            comments = Comment.objects.select_related('post').filter(post=post)
            hashtags = HashTag.objects.select_related('post').filter(post=post)
            comment_form = CommentForm()
            hashtag_form = HashTagForm()
            post.views += 1
            post.save()

            context = {
                'title': 'Blog',
                'post': post,
                'comments': comments,
                'hashtags': hashtags,
                'comment_form': comment_form,
                'hashtag_form': hashtag_form,
            }
            return render(request, 'blog/post_detail.html', context)
        except Post.DoesNotExist:
            raise Http404("존재하지 않는 게시글입니다")


class Write(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        context = {
            'title': 'Blog',
            'form': form,
        }
        return render(request, 'blog/post_form.html', context)

    def post(self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
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
        if request.user == post.writer:
            form = PostForm(
                initial={'title': post.title, 'content': post.content})
            context = {
                'title': 'Blog',
                'post': post,
                'form': form,
            }
            return render(request, 'blog/post_edit.html', context)
        return HttpResponseForbidden("수정 권한이 없습니다.")

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = PostForm(request.POST)
        if request.user == post.writer:
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
        return HttpResponseForbidden("수정 권한이 없습니다.")


class Delete(View):
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.user == post.writer:
            post.delete()
            return redirect('blog:list')
        return HttpResponseForbidden("삭제 권한이 없습니다.")


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


# ## 댓글
class CommentWrite(LoginRequiredMixin, View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(pk=pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            comment = Comment.objects.create(
                post=post, content=content, writer=writer)
            return redirect('blog:detail', pk=pk)

        hashtag_form = HashTagForm()
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': form,
            'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


class CommentDelete(View):
    def post(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        post_id = comment.post.id
        if request.user == comment.writer or request.user == comment.post.writer:
            comment.delete()
            return redirect('blog:detail', pk=post_id)
        return HttpResponseForbidden("삭제 권한이 없습니다.")


class ReplyWrite(LoginRequiredMixin, View):
    def post(self, request, post_pk, comment_pk):
        form = CommentForm(request.POST)
        comment = Comment.objects.get(pk=comment_pk)

        if form.is_valid():
            content = form.cleaned_data['content']
            writer = request.user
            post = comment.post
            reply = Reply.objects.create(
                comment=comment, content=content, writer=writer)
            return redirect('blog:detail', pk=post.pk)

        hashtag_form = HashTagForm()
        context = {
            'title': 'Blog',
            'post': post,
            'comments': post.comment_set.all(),
            'hashtags': post.hashtag_set.all(),
            'comment_form': form,
            'hashtag_form': hashtag_form
        }
        return render(request, 'blog/post_detail.html', context)


class ReplyDelete(View):
    def post(self, request, pk):
        reply = Reply.objects.get(pk=pk)
        post_id = reply.comment.post.id
        if request.user == reply.writer or request.user == reply.comment.writer:
            reply.delete()
            return redirect('blog:detail', pk=post_id)
        return HttpResponseForbidden("삭제 권한이 없습니다.")


# ## 해시태그
class HashTagWrite(View):
    def post(self, request, pk):
        form = HashTagForm(request.POST)
        post = Post.objects.get(pk=pk)

        if request.user == post.writer:
            if form.is_valid():
                name = form.cleaned_data['name']
                writer = request.user
                hashtag = HashTag.objects.create(
                    post=post, name=name, writer=writer)
                return redirect('blog:detail', pk=pk)

            comment_form = CommentForm()
            context = {
                'title': 'Blog',
                'post': post,
                'comments': post.comment_set.all(),
                'hashtags': post.hashtag_set.all(),
                'comment_form': comment_form,
                'hashtag_form': form
            }
            return render(request, 'blog/post_detail.html', context)
        return HttpResponseForbidden("태그 작성은 글 작성자만 가능합니다.")


class HashTagDelete(View):
    def post(self, request, pk):
        hashtag = HashTag.objects.get(pk=pk)
        post_id = hashtag.post.id
        if request.user == hashtag.writer:
            hashtag.delete()
            return redirect('blog:detail', pk=post_id)
        return HttpResponseForbidden("삭제 권한이 없습니다.")
