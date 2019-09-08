from django.urls import path
from .import views

app_name='recognizer'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail', views.detail, name='detail'),
    path('results',views.result_view,name='result'),
]