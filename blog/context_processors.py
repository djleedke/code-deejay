
from .models import Post

def sidebar(request):

    tags = Post.tags.all()

    context = {
        'tags':tags,
    }

    return context