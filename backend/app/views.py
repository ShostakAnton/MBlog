from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View, ListView
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin  # проверка на вход в акаунт пользователя


class AllTwit(ListView):
    """Выводим все твиты"""
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'app/index.html'
    # ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwargs):       # передача формы
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        return context


class PostView(View):
    """Сообщения пользователя"""

    def get(self, request):  # возвращение сообщений от конкретного пользователя
        if request.user.is_authenticated:
            posts = Post.objects.filter(twit__isnull=True, user=request.user)
        else:
            posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()

        paginator = Paginator(posts, 5)
        page = request.GET.get("page")  # получаем номер страницы на которой сейчас находимя\ся
        page_obj = paginator.get_page(page)

        return render(request, 'app/index.html', {'posts': posts,
                                                  'form': form,
                                                  "page_obj": page_obj})

    def post(self, request):  # отправка сообщений
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)  # получаем id с фронт-енда
            form = form.save(commit=False)  # приостановка сохранения формы
            if pk is not None:
                form.twit = Post.objects.get(id=pk)  # присваеваем твит, сообщению которому соотвествует
                # полученый id
            form.user = request.user  # присваеваем к форме юзера
            form.save()
            return redirect('posts')
        else:
            return HttpResponse('error')


class Like(LoginRequiredMixin, View):
    """Ставим лайк"""

    def post(self, request):
        pk = request.POST.get("pk")
        post = Post.objects.get(id=pk)
        if request.user in post.user_like.all():
            post.user_like.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.user_like.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)
