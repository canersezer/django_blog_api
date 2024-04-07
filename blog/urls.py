from django.urls import path,include

from rest_framework import routers

from .views import BlogModelViewSet,CatagoryModelViewSet

router = routers.DefaultRouter()
router.register('categories',CatagoryModelViewSet)
router.register('blog',BlogModelViewSet)


urlpatterns = [
    path('',include(router.urls))
]
