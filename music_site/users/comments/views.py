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
from music.models import Album
from .serializers import (AlbumSerializer,
                          AlbumDetailSerializer,
                          AlbumCreateSerializer,
                          AlbumUpdateSerializer)
from .permission import IsOwnerOrReadOnly


class AlbumAPIView(ListAPIView):
    queryset = Album.objects.all().order_by('-release_date')
    serializer_class = AlbumSerializer


class DetailAlbumAPIView(RetrieveAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer


class AlbumCreateAPIView(CreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumUpdateAPIView(UpdateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDeleteAPIView(DestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumDetailSerializer


