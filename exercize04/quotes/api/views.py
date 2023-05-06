from quotes.api.serializer import QuotesSerializer
from quotes.models import quote

from rest_framework import generics
from rest_framework import mixins


class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = quote.objects.all()
    serializer_class = QuotesSerializer

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = quote.objects.all()
    serializer_class = QuotesSerializer
