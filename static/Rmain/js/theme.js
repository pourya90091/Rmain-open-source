if (localStorage.getItem("dark_theme")) {
    dark_theme(0)
}
function dark_theme(n) {
    const btn = document.getElementById("dark_theme_btn");
    const main_style = document.getElementById("main_style");
    const header_style = document.getElementById("header_style");
    const footer_style = document.getElementById("footer_style");
    const HJ_game_style = document.getElementById("HJ_game_style");
    const tetris_style = document.getElementById("tetris_style");
    const game2048_style = document.getElementById("game2048_style");
    const joke_style = document.getElementById("joke_style");
    const weather_style = document.getElementById("weather_style");
    const panel_page_style = document.getElementById("panel_page_style");
    if (n == 0) {
        try{main_style.href = "/static/Rmain/css/black_theme/main_style_black.css";}catch{}
        try{header_style.href = "/static/Rmain/css/black_theme/header_style_black.css";}catch{}
        try{footer_style.href = "/static/Rmain/css/black_theme/footer_style_black.css";}catch{}
        try{HJ_game_style.href = "/static/games_module/css/black_theme/HJ_game_style_black.css";}catch{}
        try{tetris_style.href = "/static/games_module/css/black_theme/tetris_style_black.css";}catch{}
        try{game2048_style.href = "/static/games_module/css/2048/main_black.css";}catch{}
        try{joke_style.href = "/static/blogs_module/css/black_theme/joke_style_black.css";}catch{}
        try{weather_style.href = "/static/blogs_module/css/black_theme/weather_style_black.css";}catch{}
        try{panel_page_style.href = "/static/panels_module/css/black_theme/panel_page_style_black.css";}catch{}
        btn.value = 1;
        localStorage.setItem("dark_theme", "true")
    }
    if (n == 1) {
        try{main_style.href = "/static/Rmain/css/main_style.css";}catch{}
        try{header_style.href = "/static/Rmain/css/header_style.css";}catch{}
        try{footer_style.href = "/static/Rmain/css/footer_style.css";}catch{}
        try{HJ_game_style.href = "/static/games_module/css/HJ_game_style.css";}catch{}
        try{tetris_style.href = "/static/games_module/tetris/css/tetris_style.css";}catch{}
        try{game2048_style.href = "/static/games_module/css/2048/main.css";}catch{}
        try{joke_style.href = "/static/blogs_module/css/joke_style.css";}catch{}
        try{weather_style.href = "/static/blogs_module/css/weather_style.css";}catch{}
        try{panel_page_style.href = "/static/panels_module/css/panel_page_style.css";}catch{}
        btn.value = 0;
        localStorage.removeItem("dark_theme")
    }
}
