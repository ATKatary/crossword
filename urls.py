"""
crossword url patterns
"""
from django.urls import path
from . import views

urlpatterns = [
    path("/crossword/puzzle", views.puzzle, name = "puzzle"),
    path("/crossword/autocomplete", views.autocomplete, name = "autocomplete"),
]