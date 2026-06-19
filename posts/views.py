from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post


def inicio(request):
    posts = Post.objects.all()
    return render(request, "posts/inicio.html", {"posts": posts})


def acerca(request):
    return render(request, "posts/acerca.html")


def post_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "posts/post_detalle.html", {"post": post})


@login_required
def post_crear(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detalle", pk=post.pk)
    else:
        form = PostForm()

    return render(
        request,
        "posts/post_form.html",
        {"form": form, "page_title": "Crear post", "submit_label": "Guardar post"},
    )


@login_required
def post_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("posts:detalle", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/post_form.html",
        {
            "form": form,
            "post": post,
            "page_title": "Editar post",
            "submit_label": "Actualizar post",
        },
    )


@login_required
def post_eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("posts:inicio")

    return render(request, "posts/post_confirm_delete.html", {"post": post})
