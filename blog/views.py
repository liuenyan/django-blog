from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage
from django.contrib import messages
from django.conf import settings
from .models import Post, Comment, Tag
from .forms import EditPostForm, CommentForm, EditProfileForm
from .tools import clean_html_tags, convert_to_html
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    return render(request, "index.html", context={'posts': posts})


def post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
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
                return redirect('post', post_id)
            else:
                messages.add_message(request, messages.ERROR, form.errors)
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        context['form'] = form
        context['comments'] = comments
    return render(request, 'post.html', context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.id != post.author.id:
        return redirect('post', post_id)
    if request.method == 'POST':
        form = EditPostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.slug = form.cleaned_data['slug']
            post.body_markdown = form.cleaned_data['body_markdown']
            post.body_html = convert_to_html(form.cleaned_data['body_markdown'])
            tags = [Tag.objects.get_or_create(tag=tag)[0] \
                    for tag in filter(None, form.cleaned_data['tags'].split(','))]
            post.categories = form.cleaned_data['categories']
            post.tags.set(tags)
            post.save()
            messages.add_message(request, messages.SUCCESS, '文章已更新')
            return redirect('post', post_id)
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    data = {
        'title': post.title,
        'slug': post.slug,
        'body_markdown': post.body_markdown,
        'tags': ','.join([t.tag for t in post.tags.all()]),
        'categories': post.categories.all(),
    }
    form = EditPostForm(data)
    return render(request, 'edit_post.html', {'form': form})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = EditPostForm(request.POST)
        if form.is_valid():
            post = Post(
                title=form.cleaned_data['title'],
                slug=form.cleaned_data['slug'],
                body_markdown=form.cleaned_data['body_markdown'],
                body_html=convert_to_html(form.cleaned_data['body_markdown']),
                author=request.user
            )
            post.save()
            tags = [Tag.objects.get_or_create(tag=tag)[0] \
                    for tag in filter(None, form.cleaned_data['tags'].split(','))]
            post.tags.set(tags)
            post.categories=form.cleaned_data['categories']
            post.save()
            messages.add_message(request, messages.SUCCESS, '文章已发布')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    form = EditPostForm()
    return render(request, 'edit_post.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.id != post.author.id:
        return redirect('post', post_id)
    post.delete()
    return redirect('index')


def tag(request, tagname):
    tag = get_object_or_404(Tag, tag=tagname)
    post_list = tag.post_set.order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    title = '标签为{0}的文章'.format(tagname)
    return render(request, 'index.html', context={'title': title, 'posts': posts})

def archive(request, year, month):
    post_list = Post.objects.filter(creation_time__year=year, creation_time__month=month).order_by('-id')
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
    return render(request, 'profile.html')

@login_required
def change_profile(request):
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
