from .models import Query, News

import os
import json
import pytz
import datetime

from django.conf import settings
from elasticsearch import Elasticsearch

es = Elasticsearch()


class Service(object):
    pass


class QueryService(Service):
    @staticmethod
    def all():
        return Query.objects.all()

    @staticmethod
    def update_by_id(id, **kwargs):
        Query.objects.filter(id=id).update(**kwargs)


class NewsService(Service):
    @staticmethod
    def all():
        return News.objects.all()

    @staticmethod
    def create(**kwargs):
        News.objects.create(**kwargs)

    @staticmethod
    def get_last_published_at_indexed():
        if os.path.exists(settings.CONF_FILE):
            with open(settings.CONF_FILE) as f:
                last_published_at = json.load(f).get('last_published_at')
                return datetime.datetime.strptime(last_published_at, "%Y-%m-%dT%H:%M:%S")
        else:
            return NewsService().save_last_published_at_indexed()

    @staticmethod
    def save_last_published_at_indexed(last_published_at=datetime.datetime(1970, 1, 1, 0, 0, tzinfo=pytz.UTC)):
        with open(settings.CONF_FILE, 'w') as f:
            json.dump({
                'last_published_at': datetime.datetime.strftime(last_published_at, "%Y-%m-%dT%H:%M:%S")
            }, f)
        return last_published_at

    @staticmethod
    def get_recent_news_by_date(last_published_at):
        return News.objects.filter(published_at__gt=last_published_at)

    @staticmethod
    def get_buckets(candidate, gte='', lte='', interval="1h"):
        res = es.search(
            index='news',
            body={
                "size": 0,
                "query": {
                    "bool": {
                        "must": {
                            "term": {"candidate": candidate}
                        },
                        "filter": {
                            "range": {
                                "published_at": {
                                    "gte": "2018-08-19T00:00:00.000Z",
                                    "lte": "2018-08-20T00:00:00.000Z",
                                }
                            }
                        }
                    }
                },
                "aggs": {
                    "number_news": {
                        "date_histogram": {
                            "field": "published_at",
                            "interval": interval
                        }
                    }
                }

            }
        )



        return res['aggregations']['number_news']['buckets']
