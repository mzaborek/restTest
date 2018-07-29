from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CreateMoviesView, CreateCommentsView

urlpatterns = {
    url(r'^movies/$', CreateMoviesView.as_view(), name="createcomment"),
    url(r'^comments/$', CreateCommentsView.as_view(), name="createmovie")
}

urlpatterns = format_suffix_patterns(urlpatterns)
