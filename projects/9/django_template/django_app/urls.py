from django.contrib import admin
from django.urls import path, include, re_path
from django_app import views

from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "is_staff"]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("react/", views.react, name="react"),
    path("test_cache/", views.test_cache, name="test_cache"),
    path("celer/", views.celer, name="celer"),
    path("celer/res/<str:res>/", views.celer_res, name="celer_res"),
    path("without_celery/", views.without_celery, name="without_celery"),
    path("position/", views.position_create),
    path("", views.Home.as_view(), name=""),
    path("index/", views.Home.as_view(), name="index"),
    # path("home/", views.Home.as_view(), name="home"),
    re_path(r"^home/", views.Home.as_view(), name="home"),
    re_path(r"^contact/(?P<contact_id>\d+)/delete/$", views.contact_delete, name="contact_delete"),
    #
    path("index_http/", views.index_http, name="index_http"),
    path("index_json/", views.index_json, name="index_json"),
    # TODO: DRF API
    path("api/contacts/", views.get_contacts, name="get_contacts"),
    #
    # path("<str:question_id>/vote/", views.index_json, name="index_json"),
    # re_path(r"^(?P<question_id>\d+)/vote/$", views.index_json, name="index_json"),
    # path('todo/<int:todo_id>/update/', views.update, name='update'),
    # re_path(r"^todo/(?P<todo_id>\d+)/update/$", views.update, name="update"),
]
