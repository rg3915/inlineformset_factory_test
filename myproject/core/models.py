import os
import uuid
from django.contrib.auth.models import User
from django.db import models


def file_path(instance, filename):
    path = "media/"
    return os.path.join(path, filename)


class TaskAnswer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    candidate = models.ForeignKey(User)
    answer_file = models.FileField(upload_to=file_path, null=True, blank=True)

    def __str__(self):
        return str(self.candidate)


class TaskAnswerFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task_answer = models.ForeignKey(TaskAnswer)
    answer_file = models.FileField(upload_to=file_path, null=True, blank=True)

    def __str__(self):
        return str(self.answer_file)
