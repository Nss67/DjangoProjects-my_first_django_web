from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views import generic

from .models import Post, Comment
from .forms import PostForm


def index(request):
    # body
    return HttpResponse("<h1>Hello, World.</h1><br><h2>This my first web site.</h2>")


def home(request):
    return HttpResponse("<h3>Welcome to my home page...</h3>")


def post_list(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/post_list.html", context=context)


class PostList(generic.ListView):
    query_set = Post.objects.all()
    template_name = "posts/post_list.html"
    context_object_name = "posts"


def post_detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, "posts/http404.html", status=404)
    comment = Comment.objects.filter(post=post)
    context = {"post": post, "comment": comment}
    return render(request, "posts/post_detail.html", context=context)


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            print(type(form.cleaned_data))
            print(form.cleaned_data)
            Post.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/posts/")
    else:
        form = PostForm()

    return render(request, "posts/post_create.html", {"form": form})

