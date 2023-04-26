from django.urls import path
from quotes.api.views import QuoteListCreate

urlpatterns = [
    path("quotes/",
         QuoteListCreate.as_view(),
         name="quotes-list"),
]
