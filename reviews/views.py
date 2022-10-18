from rest_framework.views import APIView,Request,Response,status
from rest_framework.authentication import TokenAuthentication
from .permissions import ReviewRotesPermition,ReviewRotesPermitionDetail
from .serializers import ReviewSerializer
from movies.models import Movie
from .models import Review
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class ReviewView(APIView,PageNumberPagination):
     authentication_classes=[TokenAuthentication]
     permission_classes=[ReviewRotesPermition]
    
     def post(self,request:Request,movie_id:int):
        movie=get_object_or_404(Movie,id=movie_id)
        serializer=ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        review_alredy_exist= Review.objects.filter(movie_id=movie.id,critic=request.user.id)
        
        if review_alredy_exist:
            return Response({"detail": "Review already exists."},status.HTTP_403_FORBIDDEN)
            
        serializer.save(movie=movie,critic=request.user)
        return Response(serializer.data,status.HTTP_201_CREATED)
         
     def get(self,request:Request,movie_id:int):
         movie=get_object_or_404(Movie,id=movie_id)
         review= Review.objects.filter(movie_id=movie.id)
         result_page = self.paginate_queryset(review, request, view=self)
         serializer=ReviewSerializer(review,many=True)
         return self.get_paginated_response(serializer.data)
         
         
class ReviewDetailView(APIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[ReviewRotesPermitionDetail]
    
    def get(self,request:Request,movie_id:int,review_id:int):
         movie=get_object_or_404(Movie,id=movie_id)
         review=get_object_or_404(Review,id=review_id,movie_id=movie.id)
         serializer=ReviewSerializer(review)
         return Response(serializer.data)
         
    def delete(self,request:Request,movie_id:int,review_id:int):
         movie=get_object_or_404(Movie,id=movie_id)
         review=get_object_or_404(Review,id=review_id,movie_id=movie.id)
         self.check_object_permissions(request, review.critic)
         review.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)             