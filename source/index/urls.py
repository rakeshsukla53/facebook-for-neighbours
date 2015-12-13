
from django.conf.urls import url
from index.views import RegistrationForm, ProfileTemplateView, ThreadForm, FeedTemplateView, ThreadMessageForm, FriendView
from . import views

urlpatterns = [
    url(r'^login/$', views.Login, name='login-redirect'),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^blog/$', views.Blog),
    url(r'^profile/$', ProfileTemplateView.as_view(), name='user-profile'),
    url(r'^register/$', RegistrationForm.as_view(), name='user-register'),
    url(r'^thread/$', ThreadForm.as_view(), name='user-thread'),
    url(r'^feed/$', FeedTemplateView.as_view(), name='user-feed'),
    url(r'^feed/(?P<hood_id>\w{0,50})/$', ThreadMessageForm.as_view(), name='user-message'),
    url(r'^profile/(?P<friend_id>\w{0,50})/$', FriendView.as_view(), name='user-friend'),
]
