from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from discussionapp.discussionimpl import Discussion
import ipdb


@api_view(['POST'])
def create_discusion(request):
    ipdb.set_trace()
    data=request.data
    disscussion=Discussion(data)
    result=disscussion.create_discussion()
    return Response(result,status=status.HTTP_200_OK)