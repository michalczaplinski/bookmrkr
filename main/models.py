from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=50)
    cover = models.ImageField(blank= True, null=True)
    description = models.TextField('description', blank=True)
    content = models.TextField('content', blank=True)
    date_created = models.DateTimeField('date created', auto_now=True)
    date_updated = models.DateTimeField('date updated', auto_now=True)
    owner = models.ForeignKey(User, related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)
    is_trashed = models.BooleanField(default=False)

    # like on reddit, eg. 'github.com'
    domain = models.CharField('domain', max_length=40, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.url)
