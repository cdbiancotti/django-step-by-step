from django.shortcuts import render

from .models import Post


def inicio(request):
    posts = Post.objects.all()
    return render(request, "posts/inicio.html", {"posts": posts})


def acerca(request):
    return render(request, "posts/acerca.html")
