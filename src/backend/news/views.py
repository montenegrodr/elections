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


from collections import defaultdict


@api_view(['GET'])
def aggregate_news(request):
    candidates = {}
    for query in QueryService().all():
        candidates[query.candidate.name] = NewsService().get_buckets(
            candidate=query.candidate.name,
        )

    dates = set()
    for candidate_buckets in candidates.values():
        for keys in candidate_buckets:
            dates.add(keys.get('key'))
    dates_ls = list(dates)
    dates_ls.sort()

    buckets = defaultdict(list)
    for candidate, stats in candidates.items():
        for s in stats:
            if s.get('key') in dates_ls:
                buckets[candidate].append(s.get('doc_count'))
            else:
                buckets[candidate].append(0)

    return Response({
        'labels': dates_ls,
        'data': buckets
    },
        status=200)
