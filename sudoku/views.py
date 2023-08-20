from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import sudokuSolver
import json

# Create your views here.


def index(request):
    return render(request, "sudoku/index.html")


def sudoku(request):
    return render(request, "sudoku/sudoku.html")


def stuck(request):
    return HttpResponse("stuck")


def solve(request):
    sudokuBoard = []

    if sudokuSolver.solver(sudokuBoard):
        solvedBoard = sudokuSolver.return_board(sudokuBoard)
        return render(request, "sudoku/sudoku.html", {"solvedBoard": solvedBoard})
    return HttpResponse("No solution")
