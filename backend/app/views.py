from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm


class PostView(View):
    """Сообщения пользователя"""

    def get(self, request):  # возвращение сообщений от конкретного пользователя
        posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()
        return render(request, 'app/index.html', {'posts': posts, 'form': form})

    def post(self, request):        # отправка сообщений
        form = PostForm(request.POST)
        if form.is_valid():
            pk = request.POST.get("id", None)           # получаем id с фронт-енда
            form = form.save(commit=False)      # приостановка сохранения формы
            if pk is not None:
                form.twit = Post.objects.get(id=pk)         # присваеваем твит, сообщению которому соотвествует
                # полученый id
            form.user = request.user    # присваеваем к форме юзера
            form.save()
            return redirect('/')
        else:
            return HttpResponse('error')
