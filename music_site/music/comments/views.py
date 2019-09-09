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
from music.models import (Comments,
                          Album)
from rest_framework.response import Response
from rest_framework import status
from .serializer import (CommentSerializer,
                        CommentCreateSerializer,
                        CommentUpdateSerializer)


class CommentAPIView(ListAPIView):
    queryset = Comments.objects.all().order_by('-publish_date')
    serializer_class = CommentSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)




