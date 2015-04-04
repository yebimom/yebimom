# -*- coding: utf-8 -*-

from django.db import models

# Models Helper
from django.dispatch import receiver
from django.db.models.signals import post_save

from yebimom.tasks import send_question_email


class Question(models.Model):
    user = models.ForeignKey("UserProfile")
    question_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    phone = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def _is_complete(self):
        return hasattr(self, 'answer') and True or False
    is_complete = property(_is_complete)

    def __unicode__(self):
        return "%s %s %s" % (
            not hasattr(self, 'answer') and "[X]" or "[O]",
            self.user,
            self.title
        )


@receiver(post_save, sender=Question)
def question_complete(sender, instance, created, **kwargs):
    if created:
        send_question_email.delay(instance.email, instance.phone,
                                  instance.title, instance.content)


class Answer(models.Model):
    question = models.OneToOneField(Question)
    answer_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
