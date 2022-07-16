from django.db import models

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    @property
    def json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'image': self.image.url
        }