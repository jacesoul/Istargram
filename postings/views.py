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
            title     = data['title'],
            content   = data['content'],
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
        title=Posting.objects.get(title=data['title'])
        comment=Comment.objects.create(
            title=title,
            user=data['user'],
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



class LikesView(View):
    def post(self, request):
        data=json.loads(request.body)
        user = User.objects.get(name=data['name'])
        post = Post.objects.get(title=data['title'])
        like = Like.objects.create(
            user=user,
            post=post
        )
        return JsonResponse({'MESSAGE':'SUCCESS'},status=200)


class FollowsView(View):
    def post(self, request):
        data = json.loads(request.body)
        following_user = User.objects.get(name=data['name1'])
        followed_user = User.objects.get(name=data['name2'])
        follow = Follow.objects.create(
            user = following_user,
            follow_user = followed_user
        )
        return JsonResponse({'MESSAGE':'SUCCESS'},status=200)


class UpdatePostsView(View):
    def post(self, request):
        data = json.loads(request.body)        
        title = Post.objects.get(title=data['title'])        
        title.content = data['content']
        title.save()        
        # update_content = Post.objects.filter(title=title).update(
        #     content=data['content']
        # )
        return JsonResponse({"MESSAGE":'SUCCESS'},status=200)

class DeleteCommentsView(View):
    def post(self, request):
        data = json.loads(request.body)
        comment = Comment.objects.get(id=data['id'])
        comment.delete()

        return JsonResponse({"MESSAGE":"SUCCESS"},status=200)

class CommentOfCommentsView(View):
    def post(self, request):
        data = json.loads(request.body)
        post = Post.objects.get(title=data['title'])
        user = User.objects.get(name=data['name'])
        comment = Comment.objects.get(id=data['id'])
        comment_of_comment = Comment.objects.create(
            post = post,
            user = user,
            content = data['content'],
            comment=comment
        )

        return JsonResponse({"MESSAGE":"SUCCESS"}, status=200)