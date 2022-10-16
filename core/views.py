from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
# Create your views here.


def home(request):
    blogs = BlogModel.objects.all()
    src = SocailMediaLink.objects.all()
    return render(request, 'home/index.html', {'blogs': blogs, 'src': src})


class SocailMediaLinkApiView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            link = SocailMediaLink.objects.get(pk=id)
            serializers = SocailMediaLinkSerializer(link)
            return Response({'status': 'success', "link": serializers.data}, status=status.HTTP_200_OK)
        else:
            link = SocailMediaLink.objects.all()
            serializers = SocailMediaLinkSerializer(link, many=True)
            return Response({'status': 'success', "link": serializers.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = SocailMediaLinkSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', "link": serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'errors', 'link': serializers.errors})

    def patch(self, request, pk, format=None):
        id = pk
        link = SocailMediaLink.objects.get(pk=id)
        serializers = SocailMediaLinkSerializer(
            link, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'Updated successfully'})
        return Response(serializers.errors)


class BlogModelApiView(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            blog = BlogModel.objects.get(pk=id)
            serializers = BlogModelSerializer(blog)
            return Response({'status': 'success', "blog": serializers.data}, status=status.HTTP_200_OK)
        else:
            blog = BlogModel.objects.all()
            serializers = BlogModelSerializer(blog, many=True)
            return Response({'status': 'success', "blog": serializers.data}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializers = BlogModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'success', "blog": serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'errors', 'blog': serializers.errors})

    def put(self, request, pk, format=None):
        id = pk
        blog = BlogModel.objects.get(pk=id)
        serializers = BlogModelSerializer(blog, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializers.errors)

    def patch(self, request, pk, format=None):
        id = pk
        blog = BlogModel.objects.get(pk=id)
        serializers = BlogModelSerializer(
            blog, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Updated successfully'})
        return Response(serializers.errors)

    def delete(self, request, pk, format=None):
        id = pk
        blog = BlogModel.objects.get(pk=id)
        blog.delete()
        return Response({"Message": "Data Deleted Successfully"})
