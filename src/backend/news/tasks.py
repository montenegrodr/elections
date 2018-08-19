from __future__ import absolute_import, unicode_literals

import time
import pytz
import logging
import aylien_news_api

from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from aylien_news_api.rest import ApiException
from .services import QueryService, NewsService

# create an instance of the API class
api_instance = aylien_news_api.DefaultApi()
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = settings.NEWSAPI_ID
aylien_news_api.configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = settings.NEWSAPI_KEY


logger = logging.getLogger(__name__)


def handle_date(last_searched_at):
    retval = datetime.now() - timedelta(seconds=settings.NEWSAPI_SIT_WAIT)
    if last_searched_at:
        retval = last_searched_at + timedelta(seconds=1)
    return retval.strftime("%Y-%m-%dT%H:%M:%S") + 'Z'


@shared_task
def fetch_news():
    logger.info('Starting to fetch news from newsapi')
    for query in QueryService().all():
        logger.info(f'Running query={query.query}')
        params = {
            'text': query.query,
            'language': ['pt'],
            'published_at_start': handle_date(query.last_searched_at),
            'cursor': '*',
            'per_page': settings.NEWSAPI_PAGE,
            'sort_by': 'published_at',
            'sort_direction': 'asc'
        }
        stories = []
        while True:
            try:
                response = api_instance.list_stories(**params)
                if not response.stories:
                    break
                stories.extend(response.stories)
                params['cursor'] = response.next_page_cursor
            except ApiException as e:
                logger.warning(f'Usage limit exceeded. {e}')
                time.sleep(60)

        if not stories:
            continue

        logger.info(f'Found {len(stories)} stories')

        last_searched_at = datetime(1, 1, 1, 0, 0, tzinfo=pytz.UTC)
        for story in stories:
            NewsService.create(
                title=story.title,
                body=story.body,
                source=story.source.name,
                source_url=story.source.home_page_url,
                author=story.author.name,
                facebook=sum([s.count for s in story.social_shares_count.facebook]),
                googleplus=sum([s.count for s in story.social_shares_count.google_plus]),
                linkedin=sum([s.count for s in story.social_shares_count.linkedin]),
                published_at=story.published_at,
                canonical=story.links.canonical,
                permalink=story.links.permalink,
                candidate=query.candidate
            )
            last_searched_at = max(last_searched_at, story.published_at)

        QueryService.update_by_id(
            id=query.id,
            last_searched_at=last_searched_at
        )


