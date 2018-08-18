from .models import Query, News


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
    def create(**kwargs):
        News.objects.create(**kwargs)
