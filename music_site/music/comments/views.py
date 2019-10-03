from rest_framework.generics import (ListAPIView,
                                    RetrieveAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView,
                                    CreateAPIView,
                                     )
from rest_framework.permissions import (IsAdminUser,
                                        IsAuthenticated,
                                        )
from music.models import (Comments,
                          Album)
from rest_framework.response import Response
from rest_framework import status
from .serializer import (CommentSerializer,
                        CommentCreateSerializer,
                        CommentUpdateSerializer,
                        CommentDeleteSerializer)
from django.http import Http404

class CommentAPIView(ListAPIView):
    queryset = Comments.objects.all().order_by('-publish_date')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentCreateAPIView(CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

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

    def put(self, request, pk, *args, **kwargs):
        obj = Comments.objects.get(id=pk)
        serializer = self.serializer_class(obj, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentDeleteSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            obj = self.get_object()
            self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)







