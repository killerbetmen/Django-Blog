from django.db import models
from django.contrib.auth.models import User


class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_title = models.CharField('Publication name', max_length=200)
    publication_text = models.TextField('Publication text')
    publication_date = models.DateTimeField('Publication date')

    def __str__(self):
        return self.publication_title

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    comment_text = models.CharField('Comment text', max_length=200)
    comment_date = models.DateTimeField('Comment time')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
