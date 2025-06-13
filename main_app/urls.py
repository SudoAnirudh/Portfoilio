from django.urls import path
from . import views

app_name = 'main_app' # Optional: for namespacing URLs

urlpatterns = [
    path('', views.index, name='home'), # Map the root of the app to the index view
]
