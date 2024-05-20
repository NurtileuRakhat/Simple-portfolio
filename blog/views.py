from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def renderPosts(request):
    posts = Post.objects.filter(author=request.user).order_by("-date")
    return render(request, "blog.html", {"posts": posts})

@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    return render(request, "post_detail.html", {"post": post})

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        post = Post.objects.create(title=title, description=description, image=image, author=request.user)
        return redirect('blog:posts')
    return render(request, 'create_post.html')
