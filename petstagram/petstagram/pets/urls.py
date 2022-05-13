from django.urls import path
from petstagram.pets import views as pets_views


urlpatterns = (
    path('', pets_views.ListPetsView.as_view(), name='list pets view'),
    path('add/', pets_views.AddPetView.as_view(), name='add pet view'),
    path('<int:pk>/', pets_views.DetailsPetView.as_view(), name='details pet view'),
    path('edit/<int:pk>', pets_views.EditPetView.as_view(), name='edit pet view'),
    path('delete/<int:pk>', pets_views.DeletePetView.as_view(), name='delete pet view'),
    path('add-photo/', pets_views.AddPetPhotoView.as_view(), name='add pet photo view'),
    path('edit-photo/', pets_views.EditPetPhotoView.as_view(), name='edit pet photo view'),
)