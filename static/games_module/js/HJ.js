function getH() {
    $.ajax({
        url: `${base_url}/games/GetHJ/H`,
        success: function (result) {
            const HJ_content = document.querySelector("#HJ-content");
            HJ_content.innerHTML = `
                    <h2>title : ${result.title}</h2>
                    <h2>description : ${result.description}</h2>
                    <h2>punishment : ${result.punishment}</h2>`
        }
    });
}
function getJ() {
    $.ajax({
        url: `${base_url}/games/GetHJ/J`,
        success: function (result) {
            const HJ_content = document.querySelector("#HJ-content");
            HJ_content.innerHTML = `
                    <h2>title : ${result.title}</h2>
                    <h2>description : ${result.description}</h2>
                    <h2>punishment : ${result.punishment}</h2>`
        }
    });
}
