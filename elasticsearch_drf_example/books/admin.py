from django.contrib import admin

from .models import (
	Author,
	Book,
	Tag,
	Publisher
)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'isbn', 'price', 'publication_date')
	search_fields = ('title',)
	filter_horizontal = ('authors', 'tags')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'email')
	search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = ('title',)


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	list_display = ('name', 'city', 'country', 'website')
