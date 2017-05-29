try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^google-analytics/$',
        views.google_analytics,
        name='google-analytics'
    ),
]
