function edit_account() {
    const url = `${Chref}-api`;

    const formData = new FormData()
    formData.append("username", document.getElementById("username").value);
    formData.append("password1", document.getElementById("password1").value);
    formData.append("password2", document.getElementById("password2").value);
    formData.append("email", document.getElementById("email").value);
    formData.append("image", document.getElementById("image").files[0]);

    $.ajax({
        url: url,
        method: "POST",
        data: formData,
        processData: false,
        contentType: false,
        enctype: "multipart/form-data",
        success: function (data, status, xhr) {
            window.location.href = data.url
            set_cookie("access_token", data.username, 1)
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
function delete_account() {
    const url = `${Chref}-api`;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            "password1": document.getElementById("password1").value,
            "password2": document.getElementById("password2").value
        },
        success: function (data, status, xhr) {
            delete_cookie("access_token")
            window.location.href = "/"
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
function email_verification(btn) {
    btn.disabled = true;

    const url = `${Chref}-api`;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            "password1": document.getElementById("password1").value,
            "password2": document.getElementById("password2").value
        },
        success: function (data, status, xhr) {
            window.location.href = data.url
            alert("email sent")
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    }).then(n => {btn.disabled = false}).catch(n => {btn.disabled = false})
}
function delete_profile_image() {
    const url = `${Chref}/delete-image-api`

    $.ajax({
        url: url,
        method: "POST",
        success: function (data, status, xhr) {
            window.location.href = data.username;
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error);
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
function recover_password_request(btn) {
    btn.disabled = true;

    const url = `${Chref}-api`;
    const email = document.getElementById("email").value

    $.ajax({
        url: url,
        method: "POST",
        data: {
            email: email
        },
        success: function (data, status, xhr) {
            // set_cookie("ACP", data.cookie_content, 0.5) // Access Change Password
            alert("email sent")
            window.location.href = "/"
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    }).then(n => {btn.disabled = false}).catch(n => {btn.disabled = false})
}
function set_new_password() {
    const url = `${Chref}-api`;

    $.ajax({
        url: url,
        method: "POST",
        data: {
            password1: document.getElementById("password1").value,
            password2: document.getElementById("password2").value,
            email: get_cookie("email")
        },
        success: function (data, status, xhr) {
            alert("password changed")
            window.location.href = data.url
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error)
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
function logout() {
    const url = `${Chref}/logout-api`

    $.ajax({
        url: url,
        method: "GET",
        success: function (data, status, xhr) {
            delete_cookie("access_token")
            window.location.href = "/"
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error);
            error.innerHTML = jqXhr.responseJSON.error
        }
    })
}
function back() {
    window.history.back()
}

// if (Chref.includes("edit-account")) {
//     const title = document.querySelector("title");
//     title.innerHTML += " - edit account"
// }
// if (Chref.includes("delete-account")) {
//     const title = document.querySelector("title");
//     title.innerHTML += " - delete account"
// }