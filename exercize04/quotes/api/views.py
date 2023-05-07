from quotes.api.serializer import QuotesSerializer
from quotes.models import quote

from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions

class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = quote.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = quote.objects.all()
    serializer_class = QuotesSerializer
