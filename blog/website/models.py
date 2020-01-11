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
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    approved = models.BooleanField(default=True)
    moreInfo = models.URLField(default='')
    def __str__(self):
        return self.title
    def titleSubtitle(self):
        return self.title + ' - ' + self.content
    def getCategoryLabel(self):
        return self.get_category_display()
    titleSubtitle.admin_order_field = 'title'

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.name
