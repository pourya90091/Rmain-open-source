function sing_up_request() {
    const url = `${Chref}api`;

    const formData = new FormData()
    formData.append("username", document.getElementById("username").value);
    formData.append("password", document.getElementById("password").value);
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
