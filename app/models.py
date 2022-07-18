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
            'image': [
                image.img.url for image in self.images()
            ],
        }
    
    def images(self) -> "list[Img]":
        return Img.objects.filter(news=self)


class Img(models.Model):
    news = models.ForeignKey(New, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images/')