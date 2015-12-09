
from django.conf.urls import url
from index.views import RegistrationForm, ProfileTemplateView, ThreadForm
from . import views

urlpatterns = [
    url(r'^login/$', views.Login, name='login-redirect'),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.Home),
    url(r'^blog/$', views.Blog),
    url(r'^profile/$', ProfileTemplateView.as_view(), name='user-profile'),
    url(r'^register/$', RegistrationForm.as_view(), name='user-register'),
    url(r'^thread/$', ThreadForm.as_view(), name='user-thread'),
]
