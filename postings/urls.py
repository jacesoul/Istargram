from django.urls import path
from postings.views import CreatePostingsView

urlpatterns = [
    path('', CreatePostingsView.as_view()),
]