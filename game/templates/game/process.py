import cv2
import numpy as np
import pytesseract

import os

script_directory = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_directory, 'example.jpg')

image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Detect and extract the grid
contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define cell dimensions based on the Sudoku grid layout
cell_height = image.shape[0] // 9
cell_width = image.shape[1] // 9

# Initialize an array to store Sudoku grid
sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

# Loop through each contour and extract digits using OCR
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cell_roi = image[y:y+h, x:x+w]

    # Perform OCR on the cell using Tesseract
    cell_text = pytesseract.image_to_string(cell_roi, config='--psm 6')

    # Clean and convert text to integer
    if cell_text.strip().isdigit():
        value = int(cell_text.strip())
        row_index = y // cell_height
        col_index = x // cell_width
        sudoku_grid[row_index][col_index] = value

# Print the Sudoku grid
for row in sudoku_grid:
    print(" ".join(str(cell) if cell != 0 else '.' for cell in row))
