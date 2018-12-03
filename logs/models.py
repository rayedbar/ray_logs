from django.db import models

class Topic(models.Model):
    """A topic the user wants to log"""
    
    name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return topic name"""

        return self.name

class Entry(models.Model):
    """A point associated with a topic"""

    topic = models.ForeignKey(Topic, models.CASCADE)
    detail = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Return the first 50 characters of entry detail"""

        return self.detail[:50] + '...'


