const Chref = window.location.href;

if (window.location.port) {
    var url = `${window.location.protocol}//${window.location.hostname}:${window.location.port}`;
}
else {
    var url = `${window.location.protocol}//${window.location.hostname}`;
}
const base_url = url;

(check_cookie)()
function set_cookie(name, content, EXdate) {
    var date = new Date();
    // date.setTime(date.getTime() + EXdate * 24 * 60 * 60 * 1000); // 1 day
    date.setTime(date.getTime() + EXdate * 60 * 60 * 1000); // 1 hour

    var expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${content};${expires};path=/`;
}
function check_cookie() {
    const username = get_cookie("access_token")
    if (username !== null) {
        const url = `${base_url}/panels/${username}/get-info-api`

        $.ajax({
                url: url,
                method: "GET",
                success: function (data, status, xhr) {
                    const profile_icon = document.getElementById("profile_icon");

                    if (data.image) {
                        profile_icon.innerHTML = `
                            <a href="${data.url}">
                                <img id="profile_image_small" src="${data.MEDIA_URL}${data.image}" alt="profile image">
                            </a>`
                    }
                    else {
                        profile_icon.innerHTML = `
                            <a href="${data.url}">
                                <img id="profile_image_small" src="" alt="profile image">
                            </a>`
                    }
                },
                error: function (jqXhr, textStatus, errorMessage) {
                    console.log(errorMessage)
                    delete_cookie("access_token")
                }
            })
    }
}
function get_cookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i <ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return null;
}
function delete_cookie(name) {
    var date = new Date();
    var expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=;${expires};path=/`;
}
