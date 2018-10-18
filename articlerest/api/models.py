from django.db import models


class Article(models.Model):
	''' This class represent Article Model '''
	title = models.CharField(max_length=255, blank=False)
	content = models.TextField(blank=False)
	author = models.CharField(max_length=100, blank=False)
	vote = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)	

	def __str__(self):
		return self.title
