from django.urls import path
from .views import MessageCreateView, MessageListView


urlpatterns = [
    path('messages/', MessageListView.as_view()),
    path('messages/create/', MessageCreateView.as_view()),
]
