from django.db import models
import uuid

class ChatRoom(models.Model):
    chatroom_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room_name = models.CharField(max_length=255)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)

class Chat(models.Model):
    chat_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    chat_type = models.CharField(max_length=1)
    message = models.TextField(null=True)
    file = models.BinaryField(null=True)
    sent_date = models.DateTimeField(auto_now_add=True)
    reply_id = models.UUIDField(null=True)