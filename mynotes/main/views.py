from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import Notes
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, CreateView, FormView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import logout, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class RegistrationForm(FormView):
    template_name = 'main/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            redirect('home')
        return super(RegistrationForm, self).form_valid(form)


class CustomLoginView(LoginView):
    form = LoginView
    template_name = 'main/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def logged_out(request):
    logout(request)
    return render(request, 'main/logged_out.html', context={})


# class CustomLogout(LogoutView):
#     form_class = LogoutView
#     template_name = 'main/logged_out.html'
#
#     def get_success_url(self):
#         return reverse_lazy('login')


class NoteList(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = 'notes'
    template_name = 'main/notes_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        return context


class CreateNote(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title', 'content', 'complete']
    context_object_name = 'create'
    template_name = 'main/create-note.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateNote, self).form_valid(form)


class NoteView(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'main/note.html'
    fields = ['title', 'content', 'complete']


class CustomUpdateView(LoginRequiredMixin, UpdateView):
    model = Notes
    context_object_name = 'update'
    fields = ['title', 'content', 'complete']
    success_url = reverse_lazy('home')


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Notes
    context_object_name = 'delete'
    success_url = reverse_lazy('home')
    template_name = 'main/delete.html'
