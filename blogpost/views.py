from django.shortcuts import render, get_object_or_404
from .models import Post, Comment


def blog_home(request):
    posts = Post.objects.order_by('-timestamp')
    recentpost = Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
        'recentposts': recentpost,
        }
    return render(request, 'blog-home.html', context)

def blog_details(request, id, title):
    post = get_object_or_404(Post, id=id, title=title)
    recentpost = Post.objects.order_by('-timestamp')
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        body = request.POST['body']
        comment = Comment.objects.create(name=name, email=email, body=body)
        if comment:
            new_comment = comment
            new_comment.post = post
            new_comment.save()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'recentposts': recentpost,
        'tags': post.tags.all
    }

    return render(request, 'blog-details.html', context)
