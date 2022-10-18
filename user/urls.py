
from django.urls import path 
from .views import LoginView, UserView,UserAdiminView,UserAdiminDetailView

urlpatterns= [
    path("register/",UserView.as_view()),
    path("login/", LoginView.as_view()),
    path("",UserAdiminView.as_view()),
    path("<int:user_id>/",UserAdiminDetailView.as_view())
]