from django.conf import settings


def google_analytics(request):
    """
    render Google Analytics tracking ID ( UA-********-* ) to template
    """
    GOOGLE_ANALYTICS_TRACKING_ID = 'UA-60220587-1'
    return {
            'GOOGLE_ANALYTICS_TRACKING_ID': GOOGLE_ANALYTICS_TRACKING_ID,
    }
