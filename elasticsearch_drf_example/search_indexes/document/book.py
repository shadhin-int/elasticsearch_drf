from django.conf import settings
from django_elasticsearch_dsl import Document, Index, Field
from elasticsearch_dsl import analyzer

from books.models import Book


