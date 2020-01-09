from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title
    def title_subtitle(self):
        return self.title + ' - ' + self.content
    title_subtitle.admin_order_field = 'title'

