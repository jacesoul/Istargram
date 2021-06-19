import json

from django.http    import JsonResponse
from django.views   import View

from .models    import Posting, User

class CreatePostingsView(View):
    def post(self, request):
        data=json.loads(request.body)

        user= User.objects.create(
            name=data['name']
        )

        posting = Posting.objects.create(
            name = user, 
            image_url = data['image_url']
        )

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)