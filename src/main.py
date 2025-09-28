"""
    Program Name: main.py
    Purpose: Starts the game by running this file.
    Inputs: N/A
    Outputs: N/A
    Collaborators: N/A
    Sources: N/A
"""
from ui import UI
def main():
    # make game + ui
    ui = UI()

    # start game
    ui.start_screen()

if __name__ == "__main__":
    main()
