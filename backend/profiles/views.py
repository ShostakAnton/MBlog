from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .models import Profile
from .forms import ProfileForm
from django.views.generic import UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages


class ProfileView(LoginRequiredMixin, DetailView):  # DetailView - ползволяет обробатывать одну запись
    """Вывод профиля пользователя"""
    model = Profile  # модель с бд
    context_object_name = 'profile'  # то как мы будем обращаться к данной переменной queryset из шаблона,
    # который будет тута передаваться
    template_name = 'profiles/profile_detail.html'  # наш шаблон

    def get_object(self, queryset=None):  # получение обьекта queryset
        obj = get_object_or_404(Profile, user=self.request.user)  # передаем модель и поля по которым делаем выборку
        if obj.user != self.request.user:  # проверка на юзера, если юзер не совпадает с тем который в базе с тем
            # который зашол на сайт
            raise Http404
        return obj


class ProfileEditView(LoginRequiredMixin, UpdateView):  # UpdateView - ползволяет делать редактирование данных
    """Редактирование профиля"""
    form_class = ProfileForm  # класс форм которые будем применять
    model = Profile
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('view_profile')  # url который будет вызван, если все пройдет успешно

    def get_object(self, queryset=None):  # обьект который будемт передаваться в темплейт
        return self.request.user.profile

    def form_valid(self, form):  # если форма дудет валидна
        messages.success(self.request, 'Profile has been updated!')
        return super().form_valid(form)


class PublicUserInfo(LoginRequiredMixin, DetailView):
    """Публичный профиль пользователя"""
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/public_user_info.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Profile, id=pk)
        return obj

    def get_queryset(self):
        profile = self.get_object()
        user = User.objects.get(id=profile.id)
        qs = user.twits.filter(twit__isnull=True)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.get_queryset()
        return context


class AddFollow(View):
    """Подпись на пользователя"""

    def post(self, request):
        pk = request.POST.get("pk")  # получаем id профеля на которого подписываемся
        user = Profile.objects.get(id=pk)  # выбираем этот профиль с бд
        user.follow.add(User.objects.get(id=request.user.id))  # добавляем в поле follow данного юзера
        user.save()
        return HttpResponse(status=201)
