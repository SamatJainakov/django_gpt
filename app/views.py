from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
import openai
import os
from dotenv import load_dotenv

from .models import Message
from .serializers import MessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save()
        message = serializer.instance.text
        answer = openai.ChatCompletion.create(
            engine='gpt-3.5-turbo',
            prompt=message,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            api_key=os.getenv('OPENAI_API_KEY'),
        )

        if answer.choices:
            answer_text = answer.choices[0].text.strip()
            answer_message = Message.objects.create(text=answer_text)
            answer_message.save()

