
from .models import Post

def sidebar(request):

    tags = Post.tags.all()
    popular_posts = Post.objects.filter(popular=True)

    context = {
        'tags':tags,
        'popular_posts':popular_posts,
    }

    return context