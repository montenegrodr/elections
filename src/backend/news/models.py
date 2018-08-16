from django.db import models


class News(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=1000)

    def __str__(self):
        return f'Model {self.id}'
