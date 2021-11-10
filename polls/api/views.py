from django.db.models import Q
from django.http import Http404
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PollSerializer

from .models import Poll, Question

class PollList(APIView):
    '''
    List all polls.
    XXX this lists all data for now. Need to list ids with titles only.
        Another view would display questions for specific poll.
    '''
    def get(self, request, format=None):
        now = timezone.now()
        polls = Poll.objects.filter(Q(start_date__lte=now) & Q(end_date__gte=now))
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

# XXX answer questions endpoint todo
