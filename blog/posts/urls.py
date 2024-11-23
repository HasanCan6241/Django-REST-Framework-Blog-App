from django.urls import path,include
from posts.views import PostViewSet,TagViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('posts',PostViewSet)
router.register('authors',AuthorViewSet)
router.register('tags',TagViewSet)

#app düzeyinde url yönlerdirmeleri
urlpatterns = [
    path('',include(router.urls))

]
