function login_request() {
    const url = `${Chref}api`;

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            username: username,
            password: password
        },
        success: function (data, status, xhr) {
            window.location.href = data.url;
            set_cookie("access_token", data.username, 1)
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
