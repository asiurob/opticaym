from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('landing/', views.landing, name="landing"),
	path('landing/crawl', views.crawl, name="crawls"),
	path('landing/crawlit', views.crawlit, name="crawlit")
]