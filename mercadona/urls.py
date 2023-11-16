from django.urls import path

from mercadona import views

urlpatterns = [
    path("", views.index, name="index"),
]
