from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^categories/$',
        views.CategoryList.as_view(),
        name='category-list'),

    url(r'^categories/(?P<pk>[0-9]+)/$',
        views.CategoryDetail.as_view(),
        name='category-detail'),

    url(r'^questions/$',
        views.QuestionList.as_view(),
        name='question-list'),

    url(r'^questions/(?P<pk>[0-9]+)/$',
        views.QuestionDetail.as_view(),
        name='question-detail')
])
