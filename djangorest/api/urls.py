from django.conf.urls import url, include
from rest_framework.urlpatterns import  format_suffix_patterns
from .views import CreateMoviesView, CreateCommentsView

urlpatterns = {
    url(r'^movies/$', CreateMoviesView.as_view(), name="create"),
    url(r'^comments/$', CreateCommentsView.as_view(), name="create")
}

urlpatterns = format_suffix_patterns(urlpatterns)