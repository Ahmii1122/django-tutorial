
from django.urls import path, include
# from watchmate_app.api.views import movie_list,movie_detail
from watchmate_app.api.views import WatchlistAV,WatchlistDetailAV,StreamPlatformAV,StreamPlatformDetailAV


urlpatterns = [
    path('list/', WatchlistAV.as_view(), name='watchlist-list'),
    path('<int:pk>', WatchlistDetailAV.as_view(), name='watchlist-detail'),
    path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
]
