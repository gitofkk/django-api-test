from django.test import TestCase
from .models import Article


class ArticleModelTestCase(TestCase):
	''' This class defines the test cases for Article Model '''

	def create_a_test_article(self):
		''' Define the test article object '''
		title = 'This is test article'
		content = 'The test article content goes like this'
		author = 'kani'
		return Article.objects.create(title=title, content=content, author=author)

	def test_article_model_can_create_a_article(self):
		''' Test the article model can create a article '''
		old_count = Article.objects.count()	
		article = self.create_a_test_article()		
		new_count = Article.objects.count()
		self.assertNotEqual(old_count, new_count)
