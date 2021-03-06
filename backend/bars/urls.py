from django.conf.urls import include, url
# from django.urls import reverse
from rest_framework.routers import DefaultRouter
from .views import (
    BarViewSet, BarViewSetAdmin, BarsDestroyAPIView,
    BarsFavoriteAPIView, BarsBookViewSet
    )

app_name = 'bars'

router = DefaultRouter()
router.register(r'bars', BarViewSet)

#Admin
router.register(r'bars_Admin', BarViewSetAdmin)  

BookBar = BarsBookViewSet.as_view({
    'post': 'create',
    'get': 'retrieve',
    'delete': 'delete',
    'put': 'update'
})

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'^bar/(?P<slug>[-\w]+)/?$',BarsDestroyAPIView.as_view()),
    url(r'^bars/(?P<bar_slug>[-\w]+)/favorite/?$',BarsFavoriteAPIView.as_view()),
    url(r'^bars/(?P<bar_slug>[-\w]+)/book/?$', BookBar, name='BookBar'),

]
