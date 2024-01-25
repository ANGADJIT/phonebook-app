from django.contrib import admin
from django.urls import path
from .views import AddContactView, ListContactsView, UpdateContactView, SearchContactView, DeleteContactView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Swagger docs configuration
schema_view = get_schema_view(
    openapi.Info(
        title="Contact APIS",
        default_version='v1',
        description="Contacts Api for managing contacts",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API routes
    path('admin/', admin.site.urls),
    path('contact/add', AddContactView.as_view()),
    path('contact/all', ListContactsView.as_view()),
    path('contact/update/<uuid:id>', UpdateContactView.as_view()),
    path('contact/search', SearchContactView.as_view()),
    path('contact/delete/<uuid:id>', DeleteContactView.as_view()),

    # Swagger DOCS route
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
