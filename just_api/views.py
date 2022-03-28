from django.shortcuts import render
from .models import Article
from .serializer import ArticleSerializer
from rest_framework import generics
from rest_framework import mixins

# Create your views here.


class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'


    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, id=None):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request)

    def delete(self, request, id=None):
        return self.destroy(request)
