# workoutwarsapp/urls.py
from django.urls import re_path
from workoutwarsapp import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

favicon_view = RedirectView.as_view(url='/static/images/myfavicon.ico', permanent=True)

urlpatterns = [
    # home page
    re_path(r'^$', views.HomePageView.as_view()),

    # authentication pages
    re_path(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    re_path(r'^signup/$', views.signup, name='signup',),

    # workout pages
    re_path(r'^add/$', views.addworkout, name='add',),
    re_path(r'^scoreboard/$', views.scoreboard, name='scoreboard',),
    re_path(r'^indiv/(?P<username>[\w.\-]+)/', views.indiv, name='indiv',),

    re_path(r'^feed/', views.feed, name='feed',),
    re_path(r'^feedscore/', views.feedscore, name='feedscore',),

    re_path(r'^rankings/$', views.rankings, name='rankings',),
    re_path(r'^coach/$', views.coach, name='coach',),

    #favicon
    re_path(r'^favicon\.ico$', favicon_view,)
]

