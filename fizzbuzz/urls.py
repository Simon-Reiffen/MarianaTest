from django.conf.urls import url, include
from fizzbuzz import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from fizzbuzz.views import fizzbuzzViewSet

router = DefaultRouter()
router.register(r'^fizzbuzz', fizzbuzzViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

]
