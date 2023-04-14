from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from django.shortcuts import get_object_or_404

class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        pk: int = self.kwargs.get("pk", None)
        return Song.objects.filter(album_id=pk)

    def perform_create(self, serializer):
        pk: int = self.kwargs.get("pk", None)
        album = get_object_or_404(Album, pk=pk)
        serializer.save(album=album)
