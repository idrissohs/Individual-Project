from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^submitidea/$', views.idea, name='idea'),
    url(r'^submitidea/thank-you/$', views.submittedIdea, name='submittedIdea'),
    url(r'^ideas/$', views.ideaListing, name='idealisting'),
    url(r'^ideas/like/(?P<pk>[0-9]+)/$', views.likeIdea, name='like'),
    url(r'^ideas/dislike/(?P<pk>[0-9]+)/$', views.dislikeIdea, name='dislike'),
)
