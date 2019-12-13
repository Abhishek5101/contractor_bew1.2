from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from entries.models import Entry
from .serializers import EntrySerializer


class EntryList(ListCreateAPIView):
    # def get(self, request):
    #     questions = Entry.objects.all()[:20]
    #     data = EntrySerializer(questions, many=True).data
    #     return Response(data)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(RetrieveDestroyAPIView):
    # def get(self, request, pk):
    #     question = get_object_or_404(Entry, pk=pk)
    #     data = EntrySerializer(question).data
    #     return Response(data)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

