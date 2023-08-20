from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from . import util
from sudoku import Sudoku
import random

# Create your views here.


def index(request):
    return render(request, "game/index.html")


def sudoku(request):
    puzzle = Sudoku(3).difficulty(0.6).board

    for row in range(len(puzzle)):
        for val in range(len(puzzle)):
            if puzzle[row][val] == None:
                puzzle[row][val] = 0

    request.session["board"] = puzzle
    print(request.session["board"])
    return render(
        request,
        "game/sudoku.html",
        {
            # generate board here
            "board": request.session["board"]
        },
    )


def stuck(request):
    return HttpResponse("stuck")


def solve(request):
    puzzle = Sudoku(3, 3, board=request.session["board"])
    solution = puzzle.solve(raising=True).board
    solvedBoard = util.listToJSON(solution)
    return render(request, "game/sudoku.html", {"board": solvedBoard})
