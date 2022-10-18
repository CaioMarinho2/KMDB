from rest_framework.views import APIView,Request,Response,status
from django.contrib.auth import authenticate
from .serializers import LoginSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdmin, IsUserOwner
from .models import User
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404

# Create your views here.

class UserView(APIView):
    def post(self, request:Request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()
        
        return Response(serializer.data,status.HTTP_201_CREATED)
    

class UserAdiminView(APIView,PageNumberPagination):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdmin]
    
    def get(self,request:Request):
        users=User.objects.all()
        result_page = self.paginate_queryset(users, request, view=self)
        serializer= UserSerializer(users,many=True)
        return self.get_paginated_response(serializer.data)
        
        
        
    

class UserAdiminDetailView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAdmin | IsUserOwner ]
    
    def get(self,request:Request,user_id:int):
        user= get_object_or_404(User,id=user_id)
        self.check_object_permissions(request, user)
        serializer=UserSerializer(user)
        
        return Response(serializer.data)   


class LoginView(APIView):
    def post(self, request:Request):
        serializer= LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN)
            
        token,created=Token.objects.get_or_create(user=user)
        return Response({"token":token.key})
            
      