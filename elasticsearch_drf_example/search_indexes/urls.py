# from django.conf.urls import url, include
# from rest_framework.routers import DefaultRouter
# from search_indexes.views.publisher import PublisherDocumentView

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.urls import urlpatterns

from search_indexes.views.publisher import PublisherDocumentView


__all__ = ('urlpatterns',)

# router = DefaultRouter()
#
# router.register(
#     r'publishers',
#     PublisherDocumentView,
#     basename='publishing'
# )