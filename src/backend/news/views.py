from rest_framework import generics
from .models import News
from .serializers import NewsSerializers


class ListNews(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class DetailNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
