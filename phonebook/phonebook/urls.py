from django.contrib import admin
from django.urls import path
from .views import AddContactView, ListContactsView, UpdateContactView, SearchContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/add', AddContactView.as_view()),
    path('contact/all', ListContactsView.as_view()),
    path('contact/update/<uuid:id>', UpdateContactView.as_view()),
    path('contact/search', SearchContactView.as_view()),
]
