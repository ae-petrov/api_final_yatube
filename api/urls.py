from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename="posts")
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename="comments")
router.register(r'follow', FollowViewSet, basename="followers")
router.register(r'group', GroupViewSet, basename="groups")


urlpatterns = [
    path('', include(router.urls)),
]
