"""
博客应用的视图函数。
"""
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from blog.models import Post, Comment, Tag, Category
from blog.forms import PostForm, CommentForm, EditProfileForm, CategoryForm, TagForm
from blog.tools import clean_html_tags, convert_to_html
# Create your views here.

def index(request):
    """首页的视图函数"""
    post_list = Post.objects.all().order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    return render(request, "index.html", context={'posts': posts})


def post_detail(request, slug):
    """文章页面的视图函数"""
    post = get_object_or_404(Post, slug=slug)
    context = {
        'comments_provider': settings.DEFAULT_COMMENTS_PROVIDER,
        'post': post,
    }
    if settings.DEFAULT_COMMENTS_PROVIDER == 'default':
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = Comment(
                    name=form.cleaned_data['name'],
                    url=form.cleaned_data['url'],
                    email=form.cleaned_data['email'],
                    comment=clean_html_tags(form.cleaned_data['comment']),
                    post=post
                )
                comment.save()
                return redirect('post', slug)
            else:
                messages.add_message(request, messages.ERROR, form.errors)
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        context['form'] = form
        context['comments'] = comments
    return render(request, 'post.html', context)


@login_required
def edit_post(request, slug):
    """文章编辑页面的视图函数"""
    post = get_object_or_404(Post, slug=slug)
    if request.user.id != post.author.id:
        return redirect('post', slug)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post.body_html = convert_to_html(post_form.cleaned_data['body_markdown'])
            post_form.save()
            messages.add_message(request, messages.SUCCESS, '文章已更新')
            return redirect('post', post.slug)
        else:
            messages.add_message(request, messages.ERROR, post_form.errors)
            context = {
                'post_form': post_form,
                'category_form': CategoryForm(),
                'tag_form': TagForm(),
            }
            return render(request, 'edit_post.html', context)
    context = {
        'post_form': PostForm(instance=post),
        'category_form': CategoryForm(),
        'tag_form': TagForm(),
    }
    return render(request, 'edit_post.html', context)


@login_required
def new_post(request):
    """文章新建页面的视图函数"""
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.body_html = convert_to_html(post_form.cleaned_data['body_markdown'])
            post.author = request.user
            post.save()
            post_form.save_m2m()
            messages.add_message(request, messages.SUCCESS, '文章已发布')
            return redirect('post', post.slug)
        else:
            messages.add_message(request, messages.ERROR, post_form.errors)
            context = {
                'post_form': post_form,
                'category_form': CategoryForm(),
                'tag_form': TagForm(),
            }
            return render(request, 'edit_post.html', context)
    context = {
        'post_form': PostForm(),
        'category_form': CategoryForm(),
        'tag_form': TagForm(),
    }
    return render(request, 'edit_post.html', context)


@login_required
def delete_post(request, slug):
    """文章删除的视图函数"""
    post = get_object_or_404(Post, id=slug)
    if request.user.id != post.author.id:
        return redirect('post', slug)
    post.delete()
    return redirect('index')


def category_posts(request, category_name):
    """分类页面的视图函数"""
    category_object = get_object_or_404(Category, category=category_name)
    post_list = category_object.post_set.order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    title = '分类为{0}的文章'.format(category_name)
    return render(request, 'index.html', context={'title': title, 'posts': posts})


@login_required
@require_POST
def new_category(request):
    """新建分类的处理函数"""
    form = CategoryForm(request.POST)
    if form.is_valid():
        category = form.save()
        result = {
            'status': 'success',
            'category': {
                'id': category.id,
                'category': category.category,
            },
        }
        return HttpResponse(json.dumps(result), content_type="text/json")
    else:
        result = {
            'status': 'fail',
            'errors': form.category.errors,
        }
        return HttpResponse(json.dumps(result), content="text/json")


@login_required
@require_POST
def new_tag(request):
    """新建标签的处理函数"""
    form = TagForm(request.POST)
    if form.is_valid():
        tag = form.save()
        result = {
            'status': 'success',
            'tag': {
                'id': tag.id,
                'tag': tag.tag,
            }
        }
        return HttpResponse(json.dumps(result), content_type="text/json")
    else:
        result = {
            'status': 'fail',
            'errors': form.errors,
        }
        return HttpResponse(json.dumps(result), content="text/json")


def tag_posts(request, tagname):
    """标签页面的视图函数"""
    tag_object = get_object_or_404(Tag, tag=tagname)
    post_list = tag_object.post_set.order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    title = '标签为{0}的文章'.format(tagname)
    return render(request, 'index.html', context={'title': title, 'posts': posts})


def archive(request, year, month):
    """归档页面的视图函数"""
    post_list = Post.objects.filter(
        creation_time__year=year,
        creation_time__month=month
    ).order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    title = '{0}年{1}月的归档'.format(year, month)
    return render(request, 'index.html', context={'title': title, 'posts': posts})


@login_required
def profile(request):
    """个人资料页面的视图函数"""
    return render(request, 'profile.html')


@login_required
def change_profile(request):
    """修改个人资料的视图函数"""
    current_user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST)
        if form.is_valid():
            current_user.first_name = form.cleaned_data['first_name']
            current_user.last_name = form.cleaned_data['last_name']
            current_user.email = form.cleaned_data['email']
            current_user.save()
            messages.add_message(request, messages.SUCCESS, '个人资料已更新')
            return redirect('profile')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    data = {
        'first_name': current_user.first_name,
        'last_name': current_user.last_name,
        'email': current_user.email
    }
    form = EditProfileForm(data)
    return render(request, 'change_profile.html', context={'form': form})
