from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Tag
from .forms import EditPostForm, CommentForm
from django.core.paginator import Paginator, InvalidPage
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=form.cleaned_data['name'], url=form.cleaned_data['url'], email=form.cleaned_data['email'], comment=form.cleaned_data['comment'], post=post)
            comment.save()
            return redirect('post', post_id)
    else:
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
        context = {
                'post': post,
                'form': form,
                'comments': comments, 
                }
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
            post.body = form.cleaned_data['body']
            tags = [Tag.objects.get_or_create(tag=tag)[0] \
                    for tag in filter(None, form.cleaned_data['tags'].split(','))]
            post.tags.set(tags)
            post.save()
            return redirect('post', post_id)
    else:
        data = {
                'title': post.title,
                'body': post.body,
                'tags': ','.join([t.tag for t in post.tags.all()]),
                }
        form = EditPostForm(data)
        return render(request, 'edit_post.html', {'form': form})


@login_required
def new_post(request):
    if request.method == 'POST':
        form = EditPostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], body=form.cleaned_data['body'], author=request.user)
            post.save()
            tags = [Tag.objects.get_or_create(tag=tag)[0] \
                    for tag in filter(None, form.cleaned_data['tags'].split(','))]
            post.tags.set(tags)
            post.save()
            return redirect('index')
    else:
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
    return render(request, 'index.html', context={'posts': posts})

def archive(request, year, month):
    post_list = Post.objects.filter(timestamp__year=year).filter(timestamp__month=month).order_by('-id')
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except InvalidPage:
        posts = paginator.page(1)
    return render(request, 'index.html', context={'posts': posts})

