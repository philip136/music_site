from rest_framework.generics import (ListAPIView,
                                    RetrieveAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView,
                                    CreateAPIView,
                                     )
from rest_framework.permissions import (AllowAny,
                                        IsAdminUser,
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        )
from music.models import Comments
from django.shortcuts import get_object_or_404
from .serializers import (AlbumSerializer,
                          AlbumDetailSerializer,
                          AlbumCreateSerializer,
                          AlbumUpdateSerializer)
from .permission import IsOwnerOrReadOnly


class AlbumAPIView(ListAPIView):
    queryset = Comments.objects.all().order_by('-publish_date')
    serializer_class = AlbumSerializer


class DetailAlbumAPIView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = AlbumDetailSerializer


class AlbumCreateAPIView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = AlbumCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AlbumUpdateAPIView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = AlbumUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class AlbumDeleteAPIView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = AlbumDetailSerializer


