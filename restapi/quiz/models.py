from django.db import models
from datetime import datetime

class Quiz(models.Model):
    name = models.CharField(max_length=256)
    date_started = models.DateField(default=datetime.now)
    date_ended = models.DateField(null=True)
    description = models.TextField(max_length=512)

    def __str__(self):
	    return self.name


class Question(models.Model):
    quiz_id = models.CharField(max_length=32)
    text = models.TextField(max_length=2048)
    type = models.CharField(max_length=1)

    def __str__(self):
	    return self.text


class Answer(models.Model):
    user_id = models.CharField(max_length=32)
    quiz_id = models.CharField(max_length=32)
    question_id = models.CharField(max_length=32)
    text = models.TextField(max_length=2048)

    def __str__(self):
	    return self.text



