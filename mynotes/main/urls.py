from django.urls import path
from .views import NoteList, RegistrationForm, CustomLoginView, CreateNote, NoteView, DeleteNote, logged_out, CustomUpdateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', NoteList.as_view(), name='home'),
    path('register/', RegistrationForm.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logged_out, name='logout'),
    path('create/', CreateNote.as_view(), name='create'),
    path('note/<int:pk>/', NoteView.as_view(), name='note'),
    path('note-delete/<int:pk>', DeleteNote.as_view(), name='delete'),
    path('note-update/<int:pk>', CustomUpdateView.as_view(), name='update'),
]