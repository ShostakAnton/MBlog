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
            window.location = response
        },
        error: (response) => {
            console.log("False")
        }
    })
};