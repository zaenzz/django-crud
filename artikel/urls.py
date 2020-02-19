from django.conf.urls import url 
from django.views.generic import (
    TemplateView,
    ListView,

    )   
from .models import Artikel
from .views import (
    ArtikelListView,
    ArtikelDetailView,
    ArtikelCategoryListView,
    ManageArtikelView,
    ArtikelCreateView,
    ArtikelUpdateView,
    ArtikelDeleteView,
    )

urlpatterns = [
    url(r'^manage/delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(), name='delete'),
    url(r'^manage/update/(?P<pk>\d+)$', ArtikelUpdateView.as_view(), name='update'),
    url(r'^create/$', ArtikelCreateView.as_view(), name='create'),
    url(r'^manage/$', ManageArtikelView.as_view(), name='manage'),
    url(r'^category/(?P<category>[\w-]+)/(?P<page>\d+)$', ArtikelCategoryListView.as_view(), name='category'),
    url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
    url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='artikel_list'),

]
