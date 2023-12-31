"""
URL configuration for grouprare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from timecatcherapi.views import register_user, check_user,UserView, TimelineView, EventView, TimelineEventView, events_by_timeline, create_timeline_and_events,CollaborativeTimelineView, CollaborativeTimelineEventView, events_by_collaborative_timeline, FollowUserView,ThreadView,FollowThreadView,ThreadCommentView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'followUsers', FollowUserView, 'followusers')
router.register(r'timelines', TimelineView, 'timeline')
router.register(r'events', EventView, 'event')
router.register(r'threads', ThreadView, 'thread')
router.register(r'followThreads', FollowThreadView, 'followThread')
router.register(r'threadComments', ThreadCommentView, 'threadComment')
router.register(r'timelineEvents', TimelineEventView, 'timelineEvent')
router.register(r'CollaborativeTimelines', CollaborativeTimelineView, 'collaborativetimeline')
router.register(r'CollaborativeTimelineEvents', CollaborativeTimelineEventView, 'collaborativetimelineevent')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
    path('api/create_timeline_and_events', create_timeline_and_events, name='create_timeline_and_events'),
    path('timeline-events/<int:pk>/events-by-timeline', events_by_timeline, name='events-by-timeline'),
    path('collaborative-timeline-events/<int:pk>/events-by-collaborative-timeline', events_by_collaborative_timeline, name='events-by-collaborative-timeline'),
]
