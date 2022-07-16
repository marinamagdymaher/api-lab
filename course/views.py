from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework import authtoken,authentication,permissions
from rest_framework.status import *
from .models import *
from .serializers import *


# Create your views here.
@api_view(['GET'])
def overview(request):
    doc = {'overview': 'api doc',
           'List': 'return list of course',
           'List/1': 'return list of course data in details',
           }
    return Response(doc, status=HTTP_200_OK)


# Course = [
#     {'id': 1, 'name': 'lets learn program language', 'hours': '3'},
#     {'id': 2, 'name': 'Designer', 'hours': '3'},
#     {'id': 3, 'name': 'UI & UX', 'hours': '5'},
#     {'id': 4, 'name': 'Frontend developer', 'hours': '3'},
# ]


@api_view(['GET'])
def list(request, id=None):
    if (id is None):
        course = Course.objects.all()
        data = CourseSerializer(course, many=True)
        return Response(data.data, status=HTTP_200_OK)
    else:
        course = Course.objects.all(id=id)
        data = CourseSerializer(course)
        return Response(data.data, status=HTTP_200_OK)


@api_view(['GET'])
def getCourse(request, id):
    course = Course.objects.all(id=id)
    data = CourseSerializer(course)
    return Response(data.data, status=HTTP_200_OK)


@api_view(['POST'])
def insert(request):
    if 'name'in request.data and 'hours'in request.data:
        course = Course.objects.create(name=request.data['name'],hours=request.data['hours'])
        data = CourseSerializer(course)
        return Response(data.data, status=HTTP_201_CREATED)
    else:
        return Response({'error':'invalid data'}, status=HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update(request):
    if 'id' in request.data:
        course = Course.objects.get(id=request.data['id'])
        if 'name'in request.data or 'hours' in request.data:
            if 'name'in request.data:
                course.name = request.data['name']
            elif 'hours' in request.data:
                course.hours = request.data['hours']
            course.save()
            data = CourseSerializer(course)
            return Response(data.data, status=HTTP_201_CREATED)
        else:
            return Response({'error': 'no data update'}, status=HTTP_406_NOT_ACCEPTABLE)

    else:
        return Response({'error': 'invalid data'}, status=HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes ([authentication.TokenAuthentication])
@permission_classes([permissions.IsAdminUser])
def delete(request, id):
    c = Course.objects.filter(id=id).delete()
    return Response({'message': 'deleted'}, status=HTTP_200_OK)