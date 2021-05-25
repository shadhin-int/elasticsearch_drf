from django_elasticsearch_dsl_drf.constants import (
	LOOKUP_FILTER_GEO_DISTANCE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
	FilteringFilterBackend,
	OrderingFilterBackend,
	SearchFilterBackend
)

from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet

from search_indexes.document.publisher import PublisherDocument
from search_indexes.serializers.book import PublisherDocumentSerializer


class PublisherDocumentView(DocumentViewSet):
	document = PublisherDocument
	serializer_class = PublisherDocumentSerializer
	lookup_field = 'id'
	filter_backends = [
		FilteringFilterBackend,
		OrderingFilterBackend,
		SearchFilterBackend
	]
	search_fields = {
		'name', 'info', 'address', 'city', 'state_province', 'country'
	}

	filter_fields = {
		'id': None,
		'name': 'name.raw',
		'city': 'city.raw',
		'state_province': 'state_province.raw',
		'country': 'country.raw'
	}

	ordering_fields = {
		'id': None,
		'name': None,
		'city': None,
		'country': None
	}

	ordering = ('id', 'name')