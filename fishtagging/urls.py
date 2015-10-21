from django.conf.urls import url
from fishtagging import views

urlpatterns = [
    url(r'^fishtagging/species/$', views.SpeciesList.as_view()),
    url(r'^fishtagging/species/(?P<pk>[0-9]+)/$', views.SpeciesDetail.as_view()),

    url(r'^fishtagging/disposition/$', views.DispositionList.as_view()),
    url(r'^fishtagging/disposition/(?P<pk>[0-9]+)/$', views.DispositionDetail.as_view()),

    url(r'^fishtagging/landlocation/$', views.LandLocationList.as_view()),
    url(r'^fishtagging/landlocation/(?P<pk>[0-9]+)/$', views.LandLocationDetail.as_view()),

    url(r'^fishtagging/states/$', views.StatesList.as_view()),
    url(r'^fishtagging/states/(?P<pk>[0-9]+)/$', views.StatesDetail.as_view()),

    url(r'^fishtagging/taggers/$', views.TaggersList.as_view()),
    url(r'^fishtagging/taggers/(?P<pk>[0-9]+)/$', views.TaggersDetail.as_view()),
]