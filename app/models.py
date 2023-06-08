from django.db import models


class Message(models.Model):
    text = models.TextField(max_length=255)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
