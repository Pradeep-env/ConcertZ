from django.db import models
import uuid

class Concert(models.Model):
    concert_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    manager = models.ForeignKey('accounts.ManagerProfile', on_delete=models.CASCADE)
    artists = models.JSONField()
    dt_concert = models.DateTimeField()
    duration = models.IntegerField(default=1)
    description = models.TextField()
    contact = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

class ConcertTicket(models.Model):
    tier_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=50, default='normal')
    cost = models.IntegerField(default=50)
    description = models.TextField(null=True)
    points = models.IntegerField(null=True)

class AttendeeTicket(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    ticket = models.JSONField()
    cost = models.IntegerField()
    qrcode = models.BinaryField()
    status = models.BooleanField(default=False)