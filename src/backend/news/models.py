from django.db import models


class Candidate(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Candidate {self.name}'


class News(models.Model):
    title = models.CharField(max_length=1000, null=True)
    body = models.TextField(null=True)
    source = models.CharField(max_length=255, null=True)
    source_url = models.CharField(max_length=255, null=True)
    author = models.CharField(max_length=255, null=True)
    facebook = models.IntegerField(null=True)
    googleplus = models.IntegerField(null=True)
    linkedin = models.IntegerField(null=True)
    published_at = models.DateTimeField(null=False)
    permalink = models.CharField(max_length=1000, null=True)
    canonical = models.CharField(max_length=1000, null=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f'News {self.id}'


class Query(models.Model):
    query = models.CharField(max_length=255)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    last_searched_at = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return f'Query {self.query}'
