from django.urls import path
from petstagram.profiles import views as profile_views

urlpatterns = (
    path('<int:pk>/', profile_views.ShowProfileView.as_view(), name='show profile view'),
    path('edit-profile/<int:pk>/', profile_views.EditProfileView.as_view(), name='edit profile view'),
    path('delete-profile/<int:pk>/', profile_views.DeleteProfileView.as_view(), name='delete profile view'),
)