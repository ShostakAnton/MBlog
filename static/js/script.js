// Установка csrf_token
(function () {                                      // авто добавление Cookie: csrftoken=gv8B1iQ5GnQ9UIoVaAckkjN4PNSauk0QSokZ13nETZGDkYjAOwFeNZ5is17AQgVY;
    let csrftoken = Cookies.get('csrftoken');       // получение csrftoken
    $.ajaxSetup({                                   // любой ajax запрос будет идти с csrftoken
        headers: {"X-CSRFToken": csrftoken}         // запись csrftoken в headers ajax
    });
})();


// Показать форму комментария
let openForm = function (id) {
    $(`#${id}`).show()
};

// Закрыть форму комментария
let closeForm = function (id) {
    $(`#${id}`).hide()
};

// Поставить лайк
let like = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/like/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response          // обновление страницы
        },
        error: (response) => {
            console.log("False")
        }
    })
};


// обработать форму авторизации с помощью ajax request.
$(".need_auth").submit(function (e) {
    e.preventDefault();
    var url = $(this).attr('action');
    var data = $(this).serialize();
    $.post(
        url,
        data,
        function (response) {
            window.location = response.location;
        },
    );
});

// Подписаться
let follow = function (id) {
    $.ajax({
        url: "http://127.0.0.1:8000/profile/follow/",
        type: "POST",
        data: {
            pk: id,
        },
        success: (response) => {
            window.location = response
        },
        error: (response) => {
            console.log("False")
        }
    })
};