# -*- coding: utf-8 -*-

from django.db import models


class Question(models.Model):
    user = models.ForeignKey("UserProfile")
    question_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def _is_complete(self):
        return hasattr(self, 'answer') and True or False
    is_complete = property(_is_complete)

    def __unicode__(self):
        return "%s %s" % (
            self.user,
            not hasattr(self, 'answer') and "Need answer" or ""
        )

class Answer(models.Model):
    question = models.OneToOneField(Question)
    answer_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
