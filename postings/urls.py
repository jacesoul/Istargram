from django.urls import path
from postings.views import CreatePostingsView, CreateCommentsView, LikesView, FollowsView, UpdatePostsView, DeleteCommentsView, CommentOfCommentsView

urlpatterns = [
    path('/posting', CreatePostingsView.as_view()),
    path('/comment', CreateCommentsView.as_view()),
    path('/like', LikesView.as_view()),
    path('/follow', FollowsView.as_view()),
    path('/update_post', UpdatePostsView.as_view()),
    path('/delete_comment', DeleteCommentsView.as_view()),
    path('/comment_of_comment', CommentOfCommentsView.as_view())
    
]