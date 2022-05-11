from django.urls import path

from petstagram.auth_app import views

urlpatterns = (
    path('sign-up/', views.SignUpView.as_view(), name='sign up view'),
    path('sign-in/', views.SignInView.as_view(), name='sign in view'),
)