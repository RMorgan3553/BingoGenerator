"""
Bingo Sheet and Tick Sheet Generator

This script reads song titles from a CSV file and generates a PDF file with 100 unique bingo sheets, each containing 25 song titles, and a tick sheet for the host to mark off played songs.

Author: Reece Morgan
Date: 08-03-2024
Usage: Execute this script with Python after placing a CSV file named 'songs.csv' in the same directory. 
       The script outputs 'bingo_sheets.pdf' and 'tick_sheet.pdf'.

Requirements: 
- Python 3.x
- reportlab library (Install using `pip install reportlab`)
"""

import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from random import shuffle

def read_song_titles(filename):
    """
    Reads song titles from a specified CSV file.
    
    Parameters:
    - filename (str): The name of the CSV file to read from.

    Returns:
    - list[str]: A list of song titles.
    """
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        song_reader = csv.reader(csvfile)
        return [row[0] for row in song_reader]

def create_bingo_sheets(songs, filename="bingo_sheets.pdf"):
    """
    Generates a PDF file containing 100 unique bingo sheets from a list of song titles.
    
    Parameters:
    - songs (list[str]): The list of shuffled song titles.
    - filename (str): The output PDF file name.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    num_sheets = 100
    grid_size = 5
    start_x, start_y = 50, height - 50
    cell_width = (width - 100) / grid_size
    cell_height = 100

    for sheet in range(num_sheets):
        current_songs = songs[sheet * 25:(sheet + 1) * 25]  # Adjust based on actual size if needed
        for i in range(grid_size):
            for j in range(grid_size):
                idx = i * grid_size + j
                song_title = "FREE" if i == grid_size // 2 and j == grid_size // 2 else current_songs[idx]
                x = start_x + j * cell_width
                y = start_y - i * cell_height
                c.rect(x, y - cell_height, cell_width, cell_height)
                c.drawString(x + 10, y - cell_height / 2, song_title)
        c.showPage()
    c.save()

def create_tick_sheet(songs, filename="tick_sheet.pdf"):
    """
    Generates a tick sheet PDF for the host, listing all song titles.
    
    Parameters:
    - songs (list[str]): The list of song titles.
    - filename (str): The output PDF file name.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    start_x, start_y = 50, height - 50
    gap = 20

    for idx, song in enumerate(songs, start=1):
        y = start_y - (idx * gap)
        if y < 50:
            c.showPage()
            start_y = height - 50
            y = start_y - (idx * gap) % start_y
        c.drawString(start_x, y, f"{idx}. {song}")

    c.save()

# Main execution
if __name__ == "__main__":
    song_titles = read_song_titles("songs.csv")
    shuffle(song_titles)
    create_bingo_sheets(song_titles)
    create_tick_sheet(song_titles)
