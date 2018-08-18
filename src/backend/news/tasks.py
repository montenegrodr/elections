from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.conf import settings


@shared_task
def fetch_news():
    queries = (
        'Jair bolsonaro'
    )

