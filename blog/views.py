from django.http.response import JsonResponse
from django.views.generic.detail import DetailView
from .forms import BlogForm
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView
from .models import Blog
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import F
# Create your views here.


def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('postid'))
        post = get_object_or_404(Blog, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.like_count -= 1
            result = post.like_count
            post.save()
        else:
            post.likes.add(request.user)
            post.like_count += 1
            result = post.like_count
            post.save()

        return JsonResponse({'result': result})


class BlogView(ListView):
    queryset = Blog.objects.filter(status=True)
    context_object_name = 'blogs'


class BlogDetailsView(DetailView):
    model = Blog
    context_object_name = 'blog'

    def get_object(self):
        obj = super().get_object()
        obj.post_views += 1
        obj.save()
        return obj


class OwnBlogView(ListView):
    queryset = Blog.objects.all()
    context_object_name = 'blogs'
    template_name = 'blog/myblog.html'

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class InsertBlog(UserPassesTestMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('ownBlog')

    def test_func(self):
        return self.request.user.user_type.startswith('DOCTOR')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(InsertBlog, self).form_valid(form)


class BlogUpdate(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('ownBlog')

    def test_func(self):
        return self.request.user.user_type.startswith('DOCTOR')

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('ownBlog')

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
