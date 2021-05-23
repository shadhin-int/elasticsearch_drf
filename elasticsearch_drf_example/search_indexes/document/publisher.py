from django.conf import settings

from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer
from books.models import Publisher
from django_elasticsearch_dsl_drf.compat import StringField, KeywordField
from django_elasticsearch_dsl_drf.analyzers import edge_ngram_completion

__all__ = ('PublisherDocument', )

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES)

INDEX.settings(
	number_of_shards=1,
	number_of_replicas=1,
	blocks={'read_only_allow_delete': False},
)


@INDEX.doc_type
class PublisherDocument(Document):

	id = fields.IntegerField(attr='id')

	name = StringField(
		fields={
			'raw': KeywordField(),
			'suggest': fields.CompletionField(),
			'edge_ngram_completion': StringField(
				analyzer=edge_ngram_completion
			),
		}
	)

	info = StringField()

	address = StringField(
		fields={
			'raw': KeywordField()
		}
	)

	city = StringField(
		fields={
			'raw': KeywordField(),
			'suggest': fields.CompletionField(),
			'edge_ngram_completion': StringField(
				analyzer=edge_ngram_completion
			),
		}
	)

	state_providence = StringField(
		fields={
			'raw': KeywordField(),
			'suggest': fields.CompletionField(),
			'edge_ngram_completion': StringField(
				analyzer=edge_ngram_completion
			),
		}
	)

	country = StringField(
		fields={
			'raw': KeywordField(),
			'suggest': fields.CompletionField(),
			'edge_ngram_completion': StringField(
				analyzer=edge_ngram_completion
			),
		}
	)

	website = StringField()

	# location
	location = fields.GeoPointField(attr='location_field_indexing')

	# Geo-Shape Field
	location_point = fields.GeoShapeField(strategy='recursive', attr='location_point_indexing')
	location_circle = fields.GeoShapeField(strategy='recursive', attr='location_circle_indexing')

	class Django(object):
		model = Publisher

	class Meta:
		parallel_indexing = True
