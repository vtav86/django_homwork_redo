"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from exercises_app.views import calculator, calculatorsub, calculatormultiply, calculatordivide, articles, show_band
from football.views import league_table, games_played
from day_3.views import converter, login, del_session \
, add_to_session, show_all_session, set_cookie, show_cookie, \
    delete_cookie, add_to_cookie, show_all_cookies
from homework_redo.views import movies, movie_details, persons, edit_person, add_person, edit_movie, add_movie, search_movie
from day3_redo.views import start_end, width_height, name, conv_temp, \
    show_scores, modify_team, test_session, set_session_redo, delete_session_redo, show_session_redo, login_redo, \
    add_to_session_redo, show_all_sessions_redo, show_cookie_redo, set_cookie_redo, delete_cookie_redo, add_to_cookie_redo, \
    show_all_cookies_redo, set_as_favourite, name_view, createBand, random3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/<int:a>/<int:b>', calculator),
    path('calculatorsub/<int:a>/<int:b>', calculatorsub),
    path('calculatormultiply/<int:a>/<int:b>', calculatormultiply),
    path('calculatordivide/<int:a>/<int:b>', calculatordivide),
    path('articles/', articles),
    path('show-band/<int:band_id>', show_band),
    path('league-table/', league_table),
    path('converter/', converter),
    path('login/', login),
    path('delete/', del_session),
    path('add-to-session/', add_to_session),
    path('show-all-session/', show_all_session),
    path('set-cookie/', set_cookie),
    path('show-cookie/', show_cookie),
    path('delete-cookie/', delete_cookie),
    path('add-to-cookie/', add_to_cookie),
    path('show-all-cookies/', show_all_cookies),
    path('games-played/', games_played),
    path('movies/', movies),
    path('movie-details/<id>/', movie_details, name="now_showing"),
    path('persons/', persons),
    path('edit-person/<id>/', edit_person),
    path('add-person/', add_person),
    path('edit-movie/<id>/', edit_movie),
    path('add-movie/', add_movie),
    path('start-end/', start_end),
    path('width-height/', width_height),
    path('name/', name),
    path('conv-temp/', conv_temp.as_view()),
    path('show-scores/', show_scores),
    path('modify-team/', modify_team),
    path('test/', test_session),
    path('search-movie/', search_movie),
    path('show-session-redo/', show_session_redo),
    path('delete-session-redo/', delete_session_redo),
    path('set-session-redo/',set_session_redo),
    path('login-redo/', login_redo),
    path('add-to-session-redo/', add_to_session_redo),
    path('show-all-sessions-redo/', show_all_sessions_redo),
    path('show-cookie-redo/', show_cookie_redo),
    path('set-cookie-redo/', set_cookie_redo),
    path('delete-cookie-redo/', delete_cookie_redo),
    path('add-to-cookie-redo/', add_to_cookie_redo),
    path('show-all-cookies-redo/', show_all_cookies_redo, name="all-cookies"),
    path('set-as-favourite/', set_as_favourite),
    path('name-view/', name_view.as_view()),
    path('create-band/', createBand.as_view()),
re_path(r'^random/(?P<min_number>\d+)/(?P<max_number>\d{2,4})/?', random3),
    path('search/', search_movie),

]
