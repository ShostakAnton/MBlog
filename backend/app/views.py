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
            return redirect('/')
        else:
            return HttpResponse('error')


class Like(View):
    """Ставим лайк"""

    def post(self, request):
        pk = request.POST.get("pk")
        post = Post.objects.get(id=pk)
        # if request.user in post.user_like.all():
        #     post.user_like.remove(User.objects.get(id=request.user.id))
        #     post.like -= 1
        # else:
        post.user_like.add(User.objects.get(id=request.user.id))
        post.like += 1
        post.save()
        return HttpResponse(status=201)
