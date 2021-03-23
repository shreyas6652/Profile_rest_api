
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from rest_framework import filters

from profiles_api import serializer
from profiles_api import models
from profiles_api import permission


class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializer.HelloSerializer

    def get(self,request,format=None):
        """Returns a List of APIView features"""
        an_apiview=[
            'Uses HTTP as function(get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over',
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})
    

    def post(self, request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)
        
       
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message='Hello '+name
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )
    def put(self,request,pk=None):
        """Handle Updating an object"""
        return Response({'method':'PUT'})
    
    def patch(self,request,pk=None):
        """Handles a parital update of an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method':'DELETE'})
         
class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    def list(self,request):
        """Returns a hello message"""
        a_viewset=[
            'Uses actions (list,create,retrieve,update,partial_update',
            'Authomatically maps to URLS using routers',
            'Provides more functionally with less code',
        ]
        return Response({'message':'Hello','Viewset1':a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializer.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permission.UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('name','email',)