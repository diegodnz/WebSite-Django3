from django.db import models

class Categories(models.TextChoices):
    tech = 'TC', 'Technology'
    health = 'HE', 'Health'
    general = 'GR', 'General'

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(
        max_length = 2,
        choices = Categories.choices,
        default = 'GR'
    )

    def __str__(self):
        return self.title

    def title_subtitle(self):
        return self.title + ' - ' + self.content

    deleted = models.BooleanField(default=True)

    title_subtitle.admin_order_field = 'title'

