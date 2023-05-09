from django.urls import path
from .views import renderIndex

urlpatterns = [
    path("", renderIndex.as_view(), name="index"),
]
