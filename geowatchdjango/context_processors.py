from __future__ import unicode_literals

from django.conf import settings

def geowatchdjango(request):
    ctx = {
        "GEOWATCH_ENABLED": settings.GEOWATCH_ENABLED,
        "GEOWATCH_STREAMING_BACKEND": settings.GEOWATCH_STREAMING_BACKEND,
        "GEOWATCH_TOPIC_PREFIX": settings.GEOWATCH_TOPIC_PREFIX
    }
    return ctx
