from django.shortcuts import render
from django.http import JsonResponse
from .tasks import fetch_cat_facts
from django.core.cache import cache

# Create your views here.


def health_check(request):
    """
    Endpoint for checking the status of the application.
    """
    return JsonResponse({ 'status': 'ok' }, status=200)


def fetch_fact(request):
    """
    Endpoint to queue an async task to fetch cat facts.
    """
    try:
        fetch_cat_facts.delay()
        return JsonResponse({ 'success': True })
    except Exception as e:
        return JsonResponse({ 'error': str(e) }, status=500)
    
    
def get_fact(request):
    """
    Endpoint to retrieve the first cat fact fetched by the `/fetch_fact` endpoint.
    """
    # Retrieve cached cat facts
    cat_facts = cache.get('cat_facts')

    if cat_facts:
        # Extract the first fact from the fetched facts
        first_fact = cat_facts[0]
        return JsonResponse({ 'fact': first_fact })
    else:
        return JsonResponse({ 'error': 'no_task_has_been_queued_yet' })
    
    