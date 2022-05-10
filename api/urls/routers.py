from rest_framework.routers import DefaultRouter

from .. import views


router = DefaultRouter()

router.register('notes', views.NoteViewSet, basename='notes')
router.register('comments', views.CommentViewSet, basename='comments')
router.register('status', views.StatusViewSet, basename='status')
