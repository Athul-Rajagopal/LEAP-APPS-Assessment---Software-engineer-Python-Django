from django.shortcuts import render
from django.http import JsonResponse
from .tasks import fetch_cat_facts

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
    # Logic to retrieve the first cat fact fetched by the `/fetch_fact` endpoint
    # For now, let's assume we have a variable `latest_fact` that stores the latest fact fetched
    latest_fact = None  # Placeholder for the latest fetched fact

    if latest_fact:
        return JsonResponse({ 'fact': latest_fact })
    else:
        return JsonResponse({ 'error': 'no_task_has_been_queued_yet' })