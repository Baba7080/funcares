from django.db import models

# Create your models here.
class UserSessionIds(models.Model):
    session_id = models.CharField(max_length=32)

class StockDetail(models.Model):
    stock = models.CharField(max_length=255, unique=True)
    user = models.ManyToManyField(UserSessionIds)