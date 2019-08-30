from django.conf.urls import url
from django.contrib import admin

from graphql_extensions.views import GraphQLView

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^graphql$", GraphQLView.as_view(graphiql=True)),
]
