import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class PublisherDocumentSerializer(DocumentSerializer):
	location = serializers.SerilizersMethodField()

	class Meta:
		fields = ('id', 'name', 'info', 'address', 'city', 'state_province', 'country', 'website')

	def get_location(self, obj):
		try:
			return obj.location.to_dict()
		except Exception:
			return {}
