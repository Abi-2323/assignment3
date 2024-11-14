from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Like
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    posts = Post.objects.all()
    user_likes = Like.objects.filter(user=request.user).values_list('post_id', flat=True)
    return render(request, "forum/dashboard.html", {"posts": posts, "user_likes": user_likes})

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Remove like if it already exists
    return redirect("dashboard")
