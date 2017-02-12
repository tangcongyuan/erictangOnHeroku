from django.conf.urls import url, include
from authentication import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # ... URLs
    url(r'^$', views.api_root),
    url(r'^accounts/$', views.AccountList.as_view(), name='account-list'),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view(), name='account-detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
