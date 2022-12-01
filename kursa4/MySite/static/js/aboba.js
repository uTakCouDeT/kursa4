$('#form').submit(function (e) {
    console.log("logging...")
    $("#error_log").removeClass("invisible");
    $("#error_log").text("Загрузка...");

    e.preventDefault();
    const url = "http://api.ukidoshi.ru/api/auth";
    const data = $('#form').serializeArray();
    console.log(data);
    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function (response) {
            console.log("success send");
            console.log(response);
            if (response["status"] === "error") {
                if (response["info"] === "wrong password") {
                    $("#error_log").text("Ошибка: неправильный пароль!");
                }
                if (response["info"] === "no such user with that email") {
                    $("#error_log").text("Ошибка: такого пользователя нет!");
                }
            }
            if (response["status"] === "success") {
                setCookie("id", response["info"]["id"]);
                setCookie("nickname", response["info"]["nickname"]);
                window.location.replace("http://messenger.ukidoshi.ru/im/");
            }
        },
        error: function (response) { // Данные не отправлены
            console.log("error");
        }
    });
});

//     e.preventDefault();
//     const url = "http://api.ukidoshi.ru/api/auth";
//     const data = $('#form').serializeArray();
//     console.log(data);
//     $.ajax({
//         type: "POST",
//         url: url,
//         data: data,
//         success: function (response) {
//             console.log("success send");
//             console.log(response);
//             if (response["status"] === "error") {
//                 if (response["info"] === "wrong password") {
//                     $("#error_log").text("Ошибка: неправильный пароль!");
//                 }
//                 if (response["info"] === "no such user with that email") {
//                     $("#error_log").text("Ошибка: такого пользователя нет!");
//                 }
//             }
//             if (response["status"] === "success") {
//                 setCookie("id", response["info"]["id"]);
//                 setCookie("nickname", response["info"]["nickname"]);
//                 window.location.replace("http://messenger.ukidoshi.ru/im/");
//             }
//         },
//         error: function (response) { // Данные не отправлены
//             console.log("error");
//         }
//     });
// });
//
// function setCookie(name, value, options = {}) {
//
//     options = {
//         path: '/',
//         ...options
//     };
//
//     if (options.expires instanceof Date) {
//         options.expires = options.expires.toUTCString();
//     }
//
//     let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);
//
//     for (let optionKey in options) {
//         updatedCookie += "; " + optionKey;
//         let optionValue = options[optionKey];
//         if (optionValue !== true) {
//             updatedCookie += "=" + optionValue;
//         }
//     }
//
//     document.cookie = updatedCookie;
// }
//
// function deleteCookie(name) {
//     setCookie(name, "", {
//         'max-age': -1
//     })
// }
//
// function getCookie(name) {
//     let matches = document.cookie.match(new RegExp(
//         "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
//     ));
//     return matches ? decodeURIComponent(matches[1]) : undefined;
// }
