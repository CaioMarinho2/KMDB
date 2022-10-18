from django.urls import path 
from .views import ReviewView, ReviewDetailView

urlpatterns= [
    path("<int:movie_id>/reviews/",ReviewView.as_view()),
    path("<int:movie_id>/reviews/<int:review_id>",ReviewDetailView.as_view())
]