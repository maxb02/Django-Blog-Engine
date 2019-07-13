from django.views.generic import View
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import TagForm, PostForm
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin


class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create_form.html'


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    form_model = PostForm
    template = 'blog/post_update_form.html'

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={
        'posts': posts,
    })


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    form_model = TagForm
    template = 'blog/tag_update_form.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={
        'tags': tags})
