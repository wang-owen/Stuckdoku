from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sudoku/solve", views.solve, name="solve"),
    path("sudoku/", views.sudoku, name="sudoku"),
    path("stuck", views.stuck, name="stuck"),
]
