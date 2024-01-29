from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    #
    path("search/", views.search, name="search"),
    path("category/", views.category, name="category"),
    path("category/<str:slug_name>/", views.f_items, name="items"),
    path("item/<str:item_id>/", views.item, name="item"),
    path("bug/<str:item_id>/", views.bug, name="bug"),
    path("comment/", views.comment, name="comment"),
    path("comment/<str:comment_id>/delete/<str:item_id>/", views.comment_delete, name="comment_delete"),
    path("public/item/", views.public, name="public"),
    path("item/hide/<str:item_id>/", views.item_hide, name="item_hide"),
    path("update/item/<str:item_id>/", views.update_item, name="update_item"),
    path("item/<str:item_id>/rating/<str:is_like>/", views.rating, name="rating"),
    path("ratings/", views.ratings, name="ratings"),
    #
    path("register/", views.register, name="register"),  # {% url 'register' %}
    path("login/", views.login_v, name="login"),
    path("logout/", views.logout_v, name="logout"),
    #
    path("test/", views.test, name="test"),
    # chat
    path("chat/", views.chat, name="chat"),
    path("chat/<slug:room_slug>/", views.room, name="room"),
    #
    # path("about/", views.about),
    path("about/", views.AboutView.as_view()),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    # moderators
    path("moderate/users/", views.moderate_users, name="moderate_users"),
    path("moderate/items/", views.moderate_items, name="moderate_items"),
    path("moderate/item/<str:item_id>/", views.moderate_item, name="moderate_item"),
]

from django_app import views_a

websocket_urlpatterns = [path("ws/chat/<slug:room_name>/", views_a.ChatConsumer.as_asgi())]
