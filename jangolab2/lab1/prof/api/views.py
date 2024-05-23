from rest_framework.response import Response
from ..models import Prof
from .serializers import ProfSerializer
from rest_framework import status
from rest_framework.decorators import api_view


@api_view(['GET'])
def list_professors(request):
    professors = Prof.objects.all()
    serialized_professors = ProfSerializer(professors, many=True)
    return Response(status=status.HTTP_200_OK, data=serialized_professors.data)


@api_view(['GET'])
def get_professor(request, id):
    professor = Prof.objects.filter(id=id).first()
    if not professor:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Professor not found'})

    serialized_professor = ProfSerializer(professor)
    return Response(status=status.HTTP_200_OK, data=serialized_professor.data)


@api_view(['PUT'])
def update_professor(request, id):
    professor_data = request.data
    professor_instance = Prof.objects.filter(id=id).first()
    if not professor_instance:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Professor not found'})

    serializer = ProfSerializer(data=professor_data, instance=professor_instance)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


@api_view(['POST'])
def create_professor(request):
    professor_data = request.data
    serializer = ProfSerializer(data=professor_data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data={'msg': 'Created'})
    return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
