from celery import shared_task
import requests
from django.core.cache import cache
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO) 

@shared_task(bind=True)
def fetch_cat_facts(self):
    try:
        response = requests.get('https://cat-fact.herokuapp.com/facts/')
        response.raise_for_status()  # Raise exception for 4xx and 5xx status codes
        facts = response.json()

        cache.set('cat_facts', facts)
        logger.info(f"Fetched cat facts: {facts}")

    except requests.RequestException as exc:
        # Log the error and retry the task
        logger.error(f"Error fetching cat facts: {exc}")
        # self.retry(exc=exc, countdown=2**self.request.retries)

    except Exception as exc:
        # Log the error and do not retry for non-network related errors
        logger.error(f"Unhandled error fetching cat facts: {exc}")

    return facts

