
from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchmate_app.api.views import movie_list,movie_detail
from watchmate_app.api.views import WatchlistAV,WatchlistDetailAV,StreamPlatformAV,StreamPlatformDetailAV,StreamPlatformVS,StreamPlatformVS
from watchmate_app.api.views import ReviewList, ReviewDetail, ReviewCreate

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='watchlist-list'),
    path('<int:pk>', WatchlistDetailAV.as_view(), name='watchlist-detail'),
    path('', include(router.urls)),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
]
