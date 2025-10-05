# Minesweeper_Group30_Project_2
Welcome to our Minesweeper PeerEnhacement GitHub page! We have all our documents, code, and more housed here. <br>
How does Minesweeper work? In this game, you can select how many bombs you want to place on the board. They will be randomly placed on the board and hidden from the user. The user has to try to click on all the non-bomb cells to win. If they suspect a cell to be a bomb, they can flag it. As the user reveals cells, they will get hints to how many bombs are adjacent to that cell they clicked on.
<br> In this addition to the project, we have added an AI featrue where the user can play with an AI bot where both will take turns to complete the game. There are three different levels: easy, medium, and hard AI mode. Each one comes with its set of challenges and strategies.
1. Easy will just uncover random cells.
2. Medium will uncover cells strategically based on two rules:
- **Rule 1:** The AI should flag all the hidden neighbors if the number of hidden neighbors of a revealed cell equals the cell’s number
- **Rule 2:** The AI should open all other hidden neighbors if the number of flagged neighbors of a revealed cell equals that cell’s number
- If rules 1 and 2 are not applied, then the AI will choose a hidden cell randomly.
3. Hard AI mode will apply all these rules of medium and a 1-2-1 rule where if three revealed cells are next to each other, and they are 1-2-1 (vertically or horizontally), then the AI should logically analyze the board to determine that the two outer covered neighbouring cells contain mines.
<br>

**Team Members - Group 30**
- Sophia Jacob
- Anna Lin
- Kusuma Murthy
- Nikka Vuong
- Nimra Syed
<br>

This project is a continuation/built off an existing repo made by:
- Sabeen Ahmad
- Anna Ross
- Sriya Annem
- Kaden Huber
- Samantha Adorno
- Tanu Sakary

**Note:** Please visit our Wiki Page at the top to see our Meeting Logs.

**Links**:
- [Team Meeting Logs](https://github.com/SAJacob7/PeerEnhancementMinesweeper_Group30_Project/wiki/Team-Meeting-Logs)
- [Sprint Board 1](https://github.com/users/SAJacob7/projects/4/views/1)

# Project Deliverables (Documentation):
- Project System Architecture and Person-Hour Estimates: Contains our diagrams of our code flow, person-hour logs, and explanation of our code.
- Meeting Logs
- Sprint Boards + Tickets
# Project Deliverables (Code):
- board.py
- ui.py
- main.py: Use this file to run the code.
# User Manual
Start by cloning this GitHub repo as seen below.
```
  git clone https://github.com/SAJacob7/PeerEnhancementMinesweeper_Group30_Project.git
```
After ensuring you have all the required modules and dependencies **and you are on the branch: project2_main**, run the main.py file by doing:
```
  python3 main.py
```
