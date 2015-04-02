# -*- coding: utf-8 -*-

from django.db import models

# Models Helper
from django.dispatch import receiver
from django.db.models.signals import post_save


class Question(models.Model):
    user = models.ForeignKey("UserProfile")
    question_date = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    content = models.TextField()


class Answer(models.Model):
    question = models.OneToOneField(Question)
    answer_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()


@receiver(post_save, sender=Answer)
def question_complete(sender, instance, created, **kwargs):
    if created:
        instance.question.is_complete = True
        instance.question.save()
