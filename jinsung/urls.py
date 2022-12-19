from django.urls import path

from jinsung.views import print_page

app_name="jinsung"

urlpatterns = [
    path("home/", print_page, name="")
]