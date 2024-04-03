from __future__ import absolute_import, unicode_literals
from celery import shared_task
import requests
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 

@shared_task(bind=True, max_retries=3)
def fetch_cat_facts(self):
    try:
        response = requests.get('https://cat-fact.herokuapp.com/facts')
        response.raise_for_status()  # Raise exception for 4xx and 5xx status codes
        facts = response.json()

        cache.set('cat_facts', facts)
        logger.info(f"Fetched cat facts: {facts}")

    except Exception as exc:
        logger.error(f"Error fetching cat facts: {exc}")
        # Retry the task up to 3 times with exponential backoff
        raise self.retry(exc=exc, countdown=2**self.request.retries)

    return facts

@shared_task
def test_celery():
    logger.info("Testing Celery: Celery is working properly!")
