from django.shortcuts import render, get_object_or_404, redirect,HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from users.models import Profile
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.blog_form import BlogCommentForm
from django.views.generic import (
    ListView,
    # DetailView,
    CreateView,
    UpdateView,
    DeleteView)

def home(request):
    context = {'posts':Post.objects.all()}
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def postDetail(request, pk):
    if request.method == 'GET':
        object_items = Post.objects.filter(id=pk)
        comments = BlogComment.objects.filter(post_id=pk)
        return render(request, 'blog/post_detail.html', {'object_items': object_items, 'comments': comments})
    if request.method == 'POST':
        comment = request.POST['comment']
        post_id = pk
        user_id = request.user
        save_comment = BlogComment(comment=comment, post_id=post_id, user_id=user_id.id)
        save_comment.save()
        return HttpResponseRedirect(reverse('post-detail', kwargs={'pk':pk}))


def writeComment(request, pk):
    if request.user.is_authenticated:
        if request.method == 'GET':
            blog_comment_form = BlogCommentForm()
            return render(request, 'blog/comment_form.html', {'blog_comment_form':blog_comment_form, 'pk':pk})
    else:
        messages.error(request, {'error_message': 'Please login to comment'})
        return redirect('login')

def about(request):
    return render(request,'blog/about.html', {'title':'vojk'})

