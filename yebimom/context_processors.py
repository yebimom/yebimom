from django.conf import settings


def google_analytics(request):
    """
    render Google Analytics tracking ID ( UA-********-* ) to template
    """
    GOOGLE_ANALYTICS_TRACKING_ID = getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_ID', False)
    if not settings.DEBUG and GOOGLE_ANALYTICS_TRACKING_ID:
        return {
                'GOOGLE_ANALYTICS_TRACKING_ID': GOOGLE_ANALYTICS_TRACKING_ID,
        }
    return {}
