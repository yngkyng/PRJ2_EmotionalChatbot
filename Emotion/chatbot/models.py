from django.db import models


class Chat(models.Model):
    query = models.CharField(max_length=500, null=False)
    answer = models.CharField(max_length=1000, null=False)

