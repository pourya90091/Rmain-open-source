var delete_count

function show_more(btn) {
    btn.disabled = true;

    const url = `${Chref}/show-more`
    const jokes = document.getElementById("jokes");

    $.ajax({
        url: url,
        method: "POST",
        data: {
            current: jokes.lastElementChild.id
        },
        success: function (data, status, xhr) {
            const new_jokes = data.new_jokes
            if (new_jokes.length > 0) {
               delete_count = new_jokes.length

                for(let i = 0 ; i < new_jokes.length ; i++) {
                    jokes.insertAdjacentHTML('beforeend', `
                        <div id="${new_jokes[i].id}" class="joke-box">
                            <h2 class="joke-title">${new_jokes[i].title}</h2>
                            <p class="text">${new_jokes[i].text}</p>
                            <hr>
                        </div>`)
                }
            }
        },
        error: function (jqXhr, textStatus, errorMessage) {
            const error = document.getElementById("error");
            alert(jqXhr.responseJSON.error);
            error.innerHTML = jqXhr.responseJSON.error
        }
    }).then(n => {btn.disabled = false})
}

function show_less() {
    const joke = document.getElementById("jokes");
    const jokes = joke.getElementsByClassName("joke-box");

    if (jokes.length > 5) {
        for (let i = 0 ; i < delete_count ; i++) {
            joke.lastElementChild.remove()
        }
        delete_count = 5
    }
}
