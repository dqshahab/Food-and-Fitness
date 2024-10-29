from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_selection, name='category_selection'),  # URL for category selection form
    path('display_workout/', views.display_workout, name='display_workout'),  # URL for displaying workout plan
]
