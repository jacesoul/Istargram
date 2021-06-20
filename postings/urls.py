from django.urls import path
from postings.views import CreatePostingsView, CreateCommentsView

urlpatterns = [
    path('/posting', CreatePostingsView.as_view()),
    path('', CreateCommentsView.as_view()),
    
]