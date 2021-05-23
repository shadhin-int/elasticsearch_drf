import json
from django.conf import settings
from django.db import models
from django.utils.translation import gettext, gettext_lazy as _

BOOK_PUBLISHING_STATUS_PUBLISHED = 'published'
BOOK_PUBLISHING_STATUS_NOT_PUBLISHED = 'not_published'
BOOK_PUBLISHING_STATUS_IN_PROGRESS = 'in_progress'
BOOK_PUBLISHING_STATUS_CANCELLED = 'cancelled'
BOOK_PUBLISHING_STATUS_REJECTED = 'rejected'
BOOK_PUBLISHING_STATUS_CHOICE = (
	(BOOK_PUBLISHING_STATUS_PUBLISHED, 'published'),
	(BOOK_PUBLISHING_STATUS_NOT_PUBLISHED, 'not_published'),
	(BOOK_PUBLISHING_STATUS_IN_PROGRESS, 'in_progress'),
	(BOOK_PUBLISHING_STATUS_CANCELLED, 'cancelled'),
	(BOOK_PUBLISHING_STATUS_REJECTED, 'rejected')
)
BOOK_PUBLISHING_STATUS_DEFAULT = BOOK_PUBLISHING_STATUS_PUBLISHED


class Publisher(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=60)
	state_providence = models.CharField(max_length=30)
	country = models.CharField(max_length=50)
	website = models.URLField()
	latitude = models.DecimalField(null=True, blank=True, decimal_places=15, max_digits=19, default=0)
	longitude = models.DecimalField(null=True, blank=True, decimal_places=15, max_digits=19, default=0)

	class Meta:
		ordering = ['id']

	def __str__(self):
		return self.name

	@property
	def location_field_indexing(self):
		return {
			'lat': self.latitude,
			'lon': self.longitude,
		}


class Book(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(null=True, blank=True)
	summary = models.TextField(null=True, blank=True)
	authors = models.ManyToManyField('books.Author', related_name='books')
	publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
	publication_date = models.DateField()
	state = models.CharField(max_length=100, choices=BOOK_PUBLISHING_STATUS_CHOICE, default=BOOK_PUBLISHING_STATUS_DEFAULT)
	isbn = models.CharField(max_length=100, unique=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	pages = models.PositiveIntegerField(default=200)
	stock_count = models.PositiveIntegerField(default=30)
	tags = models.ManyToManyField('books.Tag', related_name='books', blank=True)

	class Meta:
		ordering = ["isbn"]

	def __str__(self):
		return self.title

	@property
	def published_indexing(self):
		if self.publisher is not None:
			return self.publisher.name

	@property
	def tags_indexing(self):
		return [tag.title for tag in self.tags.all()]
