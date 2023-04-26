from quotes.api.serializer import QuotesSerializer
from quotes.models import quote

from rest_framework import generics
from rest_framework import mixins

class QuoteListCreate(
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    
    queryset = quote.objects.all()
    serializer_class = QuotesSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request,  *args, **kwargs):
       return self.list(request, *args, **kwargs)