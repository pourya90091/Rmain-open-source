from django.urls import path
from games_module import views, APIView

urlpatterns = [
    path('', views.games, name='games-page'),
    path('HJ_game', views.HJ_game, name='HJ-game-page'),
    path('tetris', views.tetris, name='tetris-page'),
    path('game2048', views.game2048, name='2048-page'),
    path('GetHJ/<str:HJ>', APIView.GetHJ.as_view())
]
