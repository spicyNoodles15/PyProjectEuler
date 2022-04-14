"""
Simple gui to interact with Project Euler solutions
"""
import os
from pathlib import Path
import PySimpleGUI as sg

#global vars
sol = 0
text = ''

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

probfont = ('Courier New', 16, 'underline')
textfont = ('Courier New', 12,)
soltext = ('Courier New', 16)

sg.theme('DarkGrey13')   # Add a touch of color

# All the stuff inside window.
layout = [[sg.Text("Enter a Problem Number:", font=textfont)],
          [sg.Input(size=(20,4), key='-INPUT-',)],
          [sg.Text(size=(40,1), key='-OUTPUT-', justification='center', font=probfont,),],
          [sg.Text(size=(60,12), key='-PROBTEXT-', justification='left', font=textfont)],
          [sg.Text(size=(40,1), key='-ANSTEXT-', justification='center', font=probfont)],
          [sg.Text(size=(40,1), key='-SOLUTION-', justification='center', font=soltext)],
          [sg.Text(size=(40,1), justification='center')],
          [sg.Button('See Problem'), sg.Button('See Answer'), sg.Button('Quit')]]

# Create the Window
window = sg.Window("Project Euler Solutions", layout, element_justification='c', location = (250, 250)).Finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    elif event == 'See Answer' or 'See Problem':
        # first clear the previous iteration of the GUI
        window['-OUTPUT-'].update('')
        window['-PROBTEXT-'].update('')
        window['-ANSTEXT-'].update('')
        window['-SOLUTION-'].update('')

        # grab all solution filenames
        solution_files = get_files()
        # check all solution file numbers to see if we have a solution for the requested problem
        for num in solution_files:
            if num == values['-INPUT-']:
                # dynamically call solution file
                exec('import solutions.problem_' + values['-INPUT-'])             
                exec('text = solutions.problem_' + values['-INPUT-'] + '.sol_text()', globals())

                # update text based on which problem was selected
                window['-OUTPUT-'].update('Problem ' + values['-INPUT-'])
                window['-PROBTEXT-'].update(text)     

                # only display the solution if the answer button has been pressed
                if event == 'See Answer':
                    exec('sol = solutions.problem_' + values['-INPUT-'] + '.solution()', globals())
                    window['-ANSTEXT-'].update("Answer:")
                    window['-SOLUTION-'].update(sol)
                break
            else:
                window['-OUTPUT-'].update("Problem Hasn't been Solved!")
window.close()