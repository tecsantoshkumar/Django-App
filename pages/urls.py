from django.urls import path
from .views import HomePageView, AboutPageView, ServicePageView  # new

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),  # new
    path("service/",ServicePageView.as_view(), name="services"),
    path("", HomePageView.as_view(), name="home"),
]
