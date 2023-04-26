from quotes.api.views import QuoteListCreate
from django.urls import path

urlpatterns = [
    path("quotes/",
         QuoteListCreate.as_view(),
         name="quotes-list")
]
