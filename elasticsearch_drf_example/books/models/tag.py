from django.db import models


class Tag(models.Model):
	title = models.CharField(max_length=255, unique=True)

	class Meta:
		"""Meta options."""

		verbose_name = "Tag"
		verbose_name_plural = "Tags"

	def __str__(self):
		return self.title
