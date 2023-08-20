from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
from . import sudokuSolver
import json

# Create your views here.


def index(request):
    return render(request, "sudoku/index.html")


def sudoku(request):
    return render(
        request,
        "sudoku/sudoku.html",
        {
            # generate board here
            "board": util.listToJSON(
                [
                    [9, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9],
                ]
            )
        },
    )


def stuck(request):
    return HttpResponse("stuck")


def solve(request):
    sudokuBoard = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]  # need to pass board here

    if sudokuSolver.solver(sudokuBoard):
        solvedBoard = util.listToJSON(sudokuBoard)
        return render(request, "sudoku/sudoku.html", {"solvedBoard": solvedBoard})
    return HttpResponse("No solution")
