from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article


class CreateArticleView(generics.ListCreateAPIView):
	queryset = Article.objects.all().order_by('-vote')
	serializer_class = ArticleSerializer

	def perform_create(self, serailizer):
		serailizer.save()

class CastVoteView(APIView):
	
	def patch(self, request, pk):
		article = get_object_or_404(Article, pk=pk)
		data = {'vote': article.vote + 1}
		serailizer = ArticleSerializer(article, data, partial=True)

		if serailizer.is_valid():
			serailizer.save()
			return Response(serailizer.data)

		return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)