const city_id = "112931";
const api_key = "de581aeeaf310e72be4d37aea69cf34e";
const weather_url = `https://api.openweathermap.org/data/2.5/weather?id=${city_id}&appid=${api_key}`

function fetch(data) {
    var temp = document.getElementById("temp");
    temp.innerHTML = Math.round(data.main.temp - 273.15) + "°C";
}

(function temp() {
    $.ajax({
        url: weather_url,
        success: function (result) {
            fetch(result)
        }
    })
})()
