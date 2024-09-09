from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entryName>", views.getEntry, name="entry"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit/<str:pageTitle>", views.edit, name="edit"),
    path("random", views.rndm, name="rndm")
]
