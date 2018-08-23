from rest_framework import generics
from .models import News
from .serializers import NewsSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import QueryService, NewsService


class ListNews(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class DetailNews(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


@api_view(['GET'])
def aggregate_news(request):
    buckets = {}
    for query in QueryService().all():
        buckets[query.candidate.name] = NewsService().get_buckets(
            candidate=query.candidate.name,
        )
    return Response(buckets, status=200)
