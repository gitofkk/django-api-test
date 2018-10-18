from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateArticleView, CastVoteView

urlpatterns = [
	path('article/lists/', CreateArticleView.as_view(), name='create_article'),
	path('article/<int:pk>/vote', CastVoteView.as_view(), name='cast_vote')	,
]

urlpatterns = format_suffix_patterns(urlpatterns)