"""
Simple gui to interact with Project Euler solutions
"""
import os
from pathlib import Path
import PySimpleGUI as sg
from solutions.problem_1 import *

def get_files():
    """
    Find all solution files
    """
    # Get current directory
    curr_path = os.getcwd()

    # empty list of solution files
    files = []

    # List all files in a directory using scandir()
    with os.scandir(curr_path + "./solutions") as entries:
        for entry in entries:
            if entry.is_file():
                # get file name and remove everything except the problem number
                files.append((Path(entry).stem).split("problem_",1)[1])
    return files

# GUI Construction

sg.theme('DarkBlue 17')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text("Enter a Problem Number:")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Text(size=(40,1), key='-PROBTEXT-')],
          [sg.Text(size=(40,1), key='-SOLUTION-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the Window
window = sg.Window("Project Euler Solutions", layout, element_justification='c', location = (250, 250)).Finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'Ok':
        # first clear the previous iteration of the GUI
        window['-OUTPUT-'].update('')
        window['-PROBTEXT-'].update('')
        window['-SOLUTION-'].update('')

        # grab all solution filenames
        solution_files = get_files()
        # check all solution file numbers to see if we have a solution for the requested problem
        for num in solution_files:
            if num is values['-INPUT-']:
                # dynamically call solution file
                # method_to_call = getattr(solutions.problem_1, 'sol_1_text')
                # result = getattr(solutions.problem_1, 'bar')()

                # update text based on which problem was selected
                window['-OUTPUT-'].update('Problem ' + values['-INPUT-'])
                window['-PROBTEXT-'].update('Result of text method call')
                window['-SOLUTION-'].update('Result of solution method call')
            else:
                window['-OUTPUT-'].update("Problem Hasn't been Solved!")
window.close()
