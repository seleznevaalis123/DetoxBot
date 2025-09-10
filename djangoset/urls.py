from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('email-signals/', include('email_signals.urls')),
    path('tinymce/', include('tinymce.urls')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
