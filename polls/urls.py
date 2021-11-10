"""polls URL Configuration
"""

from django.contrib import admin
from django.urls import path
from .api import views

urlpatterns = [
    path('polls/', views.PollList.as_view()),
    path('admin/', admin.site.urls)
]
