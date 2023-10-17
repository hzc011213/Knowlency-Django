from django.urls import path

from . import views

app_name = "chat"
urlpatterns = [
    # ex: /chat/
    path("", views.chat, name="chat"),
    path('chat/clear_history/', views.clear_history, name='clear_history'),
]
