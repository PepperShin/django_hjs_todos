from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # 빈 문자열
    created = models.DateTimeField(auto_now_add=True)  # 시간
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self):
        return self.title
