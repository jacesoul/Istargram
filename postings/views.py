import json

from django.http    import JsonResponse
from django.views   import View

from .models        import Post, User, Comment, Like, Follow
from users.models   import Signup

class CreatePostingsView(View):
    def post(self, request):
        data=json.loads(request.body)
        user    = User.objects.create(name=data['name'])
        posting = Posting.objects.create(
            name      = user, 
            image_url = data['image_url']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

    def get(self, request):
        postings = Posting.objects.all()
        results=[]
        for posting in postings:
            results.append(
                {
                    "name"       : posting.name.name,
                    "created_at" : posting.created_at,
                    "Image_url"  : posting.image_url
                }
            )
        return JsonResponse({'RESULT':results}, status=200)

class CreateCommentsView(View):
    def post(self, request):
        data=json.loads(request.body)
        title = Posting.objects.get(title=data['title'])
        comment = Comment.objects.create(
            title=title,
            comment_user=data['comment_user'],
            content = data['content']
        )
        return JsonResponse({'MESSAGE':'SUCCESS'},status=200)

    def get(self, request):
        comments = Comment.objects.filter(title_id=3)
        results=[]
        for comment in comments:
            results.append(
                {
                    "title" : comment.title.title,
                    "comment_user" : comment.comment_user,
                    "created_at" : comment.created_at,
                    "content" : comment.content
                }
            )
        return JsonResponse({"RESULT": results},status=200)

